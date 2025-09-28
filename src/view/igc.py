import sys
sys.path.append("src")

from model import monto
from model.monto import conversion_tasa_anual

try:
    # Entradas
    monto_credito = float(input("Ingrese el monto del crédito: "))
    duracion_periodo_meses = int(input("Ingrese la duración del periodo de gracia (meses): "))
    tasa_interes_anual = float(input("Ingrese la tasa de interés anual (%): "))
    plazo_amortizacion = int(input("Ingrese el plazo de amortización (meses): "))

    # Procesos
    tasa_mensual, valor_a_pagar, cuota_mensual, total, intereses = conversion_tasa_anual(
        monto_credito, duracion_periodo_meses, tasa_interes_anual, plazo_amortizacion
    )

    # Salidas
    print("\n--- RESULTADOS DEL CRÉDITO EDUCATIVO ---")
    print(f"Tasa mensual: {round(tasa_mensual*100, 2)} %")
    print(f"Capital ajustado tras periodo de gracia: ${round(valor_a_pagar, 2)}")
    print(f"Cuota mensual: ${round(cuota_mensual, 2)}")
    print(f"Total a pagar: ${total}")
    print(f"Intereses totales: ${intereses}")

except ValueError as e:
    print("Error: Los datos ingresados no son válidos -> " + str(e))
except Exception as e:
    print("Ocurrió un error inesperado: " + str(e))
