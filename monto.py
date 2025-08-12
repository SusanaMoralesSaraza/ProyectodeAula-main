def calcular_tasa_mensual(tasa_interes_anual):
    return tasa_interes_anual / 100 / 12

def calcular_valor_a_pagar(monto_credito, tasa_mensual, duracion_periodo_meses):
    return monto_credito * (1 + tasa_mensual) ** duracion_periodo_meses

def calcular_cuota_mensual_10_anios(valor_a_pagar, plazo_amortizacion):
    return valor_a_pagar / plazo_amortizacion

def calcular_total_a_pagar(cuota_mensual_10_años, plazo_amortizacion):
    return round(cuota_mensual_10_años * plazo_amortizacion, 2)

def conversion_tasa_anual(monto_credito, duracion_periodo_meses, tasa_interes_anual, plazo_amortizacion):
    tasa_mensual = calcular_tasa_mensual(tasa_interes_anual)
    valor_a_pagar = calcular_valor_a_pagar(monto_credito, tasa_mensual, duracion_periodo_meses)
    cuota_mensual_10_años = calcular_cuota_mensual_10_anios(valor_a_pagar, plazo_amortizacion)
    total_a_pagar = calcular_total_a_pagar(cuota_mensual_10_años, plazo_amortizacion)
    return tasa_mensual, valor_a_pagar, cuota_mensual_10_años, total_a_pagar

# Caso de prueba
monto_credito = 25000000
duracion_periodo_meses = 60
tasa_interes_anual = 15
plazo_amortizacion = 180

tasa_mensual, valor_a_pagar, cuota_mensual_10_años, resultado = conversion_tasa_anual(
    monto_credito, duracion_periodo_meses, tasa_interes_anual, plazo_amortizacion
)

print("Tasa mensual:", round(tasa_mensual, 2))
print("Valor a pagar:", round(valor_a_pagar, 2))
print("Cuota mensual en 10 años:", round(cuota_mensual_10_años, 2))
print("Total a pagar:", round(resultado, 2))

resultado_esperado = resultado

if abs(resultado - resultado_esperado) < 0.01:
    print("Prueba exitosa")
else:
    print("La prueba falló")


class ErrorMonto(Exception):
    """Error cuando el monto no es ingresado o es igual a cero."""

class ErrorPeriodoGracia(Exception):
    """Error cuando el periodo de gracia no es ingresado o es igual a cero."""


def calcular_valor_a_pagar(monto_credito, tasa_interes_anual, plazo_amortizacion):
    if monto_credito <= 0:
        raise ErrorMonto("El monto del crédito debe ser mayor a cero.")
    
    if plazo_amortizacion <= 0:
        raise ErrorPeriodoGracia("El plazo de amortización debe ser mayor a cero.")

