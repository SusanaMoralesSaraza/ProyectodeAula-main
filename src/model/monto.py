# src/model/monto.py

# --- Constantes para evitar "números mágicos" ---
MESES_MINIMOS_AMORTIZACION: int = 120
MESES_MAXIMOS_AMORTIZACION: int = 180


# --- Excepciones específicas ---
class ErrorMonto(ValueError):
    """El monto del crédito debe ser mayor a cero."""


class ErrorPeriodoGracia(ValueError):
    """El periodo de gracia debe ser mayor a cero."""


class ErrorDemasiadasCuotas(ValueError):
    """El plazo de amortización permitido es de 10 a 15 años (120 a 180 meses)."""


# --- Funciones de negocio ---
def calcular_tasa_mensual(tasa_interes_anual: float) -> float:
    """
    Convierte la tasa nominal anual en % a tasa efectiva mensual (en fracción).
    Ej.: 12 -> 0.01
    """
    if tasa_interes_anual <= 0:
        raise ValueError("La tasa de interés anual debe ser mayor a cero.")
    return tasa_interes_anual / 100.0 / 12.0


def calcular_valor_a_pagar(
    monto_credito: float,
    tasa_interes_anual: float,
    duracion_periodo_meses: int,
    plazo_amortizacion: int,
) -> float:
    """
    Capitaliza el monto durante el periodo de gracia a la tasa mensual.
    Valida monto, gracia y rango de plazo (120–180 meses).
    Retorna el capital ajustado al final del periodo de gracia (base para amortización).
    """
    if monto_credito <= 0:
        raise ErrorMonto("El monto del crédito debe ser mayor a cero.")
    if duracion_periodo_meses <= 0:
        raise ErrorPeriodoGracia("El periodo de gracia debe ser mayor a cero.")
    if not (MESES_MINIMOS_AMORTIZACION <= plazo_amortizacion <= MESES_MAXIMOS_AMORTIZACION):
        raise ErrorDemasiadasCuotas(
            f"El plazo de amortización debe estar entre {MESES_MINIMOS_AMORTIZACION} y {MESES_MAXIMOS_AMORTIZACION} meses."
        )

    tasa_mensual: float = calcular_tasa_mensual(tasa_interes_anual)
    # Capital ajustado después del periodo de gracia
    valor_ajustado: float = monto_credito * (1.0 + tasa_mensual) ** duracion_periodo_meses
    return valor_ajustado


def calcular_cuota_mensual(
    valor_a_pagar: float,
    tasa_mensual: float,
    plazo_amortizacion: int,
) -> float:
    """
    Cuota fija (sistema francés):
        cuota = VA * [ r / (1 - (1+r)^(-n)) ]
    """
    # Aquí tasa_mensual > 0 por validaciones previas.
    return valor_a_pagar * (tasa_mensual / (1.0 - (1.0 + tasa_mensual) ** (-plazo_amortizacion)))


def conversion_tasa_anual(
    monto_credito: float,
    duracion_periodo_meses: int,
    tasa_interes_anual: float,
    plazo_amortizacion: int,
) -> tuple[float, float, float, float, float]:
    """
    Orquesta los cálculos y retorna:
      (tasa_mensual, valor_a_pagar, cuota_mensual, total_a_pagar, intereses_totales)

    - intereses_totales = total_a_pagar - monto_credito
      (incluye tanto capitalización en gracia como los intereses de la amortización)
    """
    tasa_mensual: float = calcular_tasa_mensual(tasa_interes_anual)

    valor_a_pagar: float = calcular_valor_a_pagar(
        monto_credito=monto_credito,
        tasa_interes_anual=tasa_interes_anual,
        duracion_periodo_meses=duracion_periodo_meses,
        plazo_amortizacion=plazo_amortizacion,
    )

    cuota_mensual: float = calcular_cuota_mensual(
        valor_a_pagar=valor_a_pagar,
        tasa_mensual=tasa_mensual,
        plazo_amortizacion=plazo_amortizacion,
    )

    total_a_pagar: float = round(cuota_mensual * plazo_amortizacion, 2)
    intereses_totales: float = round(total_a_pagar - monto_credito, 2)

    return tasa_mensual, valor_a_pagar, cuota_mensual, total_a_pagar, intereses_totales
