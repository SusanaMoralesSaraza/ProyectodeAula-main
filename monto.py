class ErrorMonto(Exception):
    """Error cuando el monto no es ingresado o es igual a cero."""

class ErrorPeriodoGracia(Exception):
    """Error cuando el periodo de gracia no es ingresado o es igual a cero."""

class ErrorDemasiadasCuotas(Exception):
    """Error solo se tiene un plazo de 10 a 15 años para el crédito."""

def calcular_tasa_mensual(tasa_interes_anual):
    return tasa_interes_anual / 100 / 12

def calcular_valor_a_pagar(monto_credito, tasa_interes_anual, duracion_periodo_meses, plazo_amortizacion):
    if monto_credito <= 0:
        raise ErrorMonto("El monto del crédito debe ser mayor a cero.")
    if duracion_periodo_meses <= 0:
        raise ErrorPeriodoGracia("El periodo de gracia debe ser mayor a cero.")
    if plazo_amortizacion < 120 or plazo_amortizacion > 180:
        raise ErrorDemasiadasCuotas("El plazo de amortización debe estar entre 120 y 180 meses.")

    tasa_mensual = calcular_tasa_mensual(tasa_interes_anual)
    # Capital ajustado después del periodo de gracia
    valor_ajustado = monto_credito * (1 + tasa_mensual) ** duracion_periodo_meses
    return valor_ajustado

def calcular_cuota_mensual(valor_a_pagar, tasa_mensual, plazo_amortizacion):
    # Fórmula de anualidad (sistema francés)
    return valor_a_pagar * (tasa_mensual / (1 - (1 + tasa_mensual) ** (-plazo_amortizacion)))

def conversion_tasa_anual(monto_credito, duracion_periodo_meses, tasa_interes_anual, plazo_amortizacion):
    tasa_mensual = calcular_tasa_mensual(tasa_interes_anual)
    valor_a_pagar = calcular_valor_a_pagar(monto_credito, tasa_interes_anual, duracion_periodo_meses, plazo_amortizacion)
    cuota_mensual = calcular_cuota_mensual(valor_a_pagar, tasa_mensual, plazo_amortizacion)
    total_a_pagar = round(cuota_mensual * plazo_amortizacion, 2)
    intereses_totales = round(total_a_pagar - monto_credito, 2)
    return tasa_mensual, valor_a_pagar, cuota_mensual, total_a_pagar, intereses_totales
