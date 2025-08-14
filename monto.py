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
        raise ErrorPeriodoGracia("El plazo de amortización debe ser mayor a cero.")
    if plazo_amortizacion < 120 or plazo_amortizacion > 180:
        raise ErrorDemasiadasCuotas("El plazo de amortización debe estar entre 120 y 180 meses.")
    tasa_mensual = calcular_tasa_mensual(tasa_interes_anual)
    return monto_credito * (1 + tasa_mensual) ** duracion_periodo_meses

def calcular_cuota_mensual_10_anios(valor_a_pagar, plazo_amortizacion):
    return valor_a_pagar / plazo_amortizacion

def calcular_total_a_pagar(cuota_mensual_10_años, plazo_amortizacion):
    return round(cuota_mensual_10_años * plazo_amortizacion, 2)

def conversion_tasa_anual(monto_credito, duracion_periodo_meses, tasa_interes_anual, plazo_amortizacion):
    valor_a_pagar = calcular_valor_a_pagar(monto_credito, tasa_interes_anual, duracion_periodo_meses, plazo_amortizacion)
    tasa_mensual = calcular_tasa_mensual(tasa_interes_anual)
    cuota_mensual_10_años = calcular_cuota_mensual_10_anios(valor_a_pagar, plazo_amortizacion)
    total_a_pagar = calcular_total_a_pagar(cuota_mensual_10_años, plazo_amortizacion)
    return tasa_mensual, valor_a_pagar, cuota_mensual_10_años, total_a_pagar

# Caso de prueba
monto_credito = 25000000
duracion_periodo_meses = 60
tasa_interes_anual = 15
plazo_amortizacion = 180

tasa_mensual, valor_a_pagar, cuota_mensual_10_años, resultado = conversion_tasa_anual(
    monto_credito, duracion_periodo_meses, tasa_interes_anual, plazo_amortizacion)


resultado_esperado = 52679533.67

if abs(resultado - resultado_esperado) < 0.01:
    print("Prueba exitosa")
else:
    print("La prueba falló")

