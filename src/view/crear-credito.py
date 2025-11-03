import sys
sys.path.append("src")

from model.credito import Credito
from controlador_creditos import ControladorCreditos


# Crear una instancia del Modelo

Credito = Credito( nombre="", monto_credito="", duracion_periodo_meses="", tasa_interes_anual="", plazo_amortizacion="")

# Pedir al usuario, los datos para llenar la instancia
Credito.nombre = input( "Ingrese el nombre del usuario del credito: ")
Credito.monto_credito = float( input("Ingrese el monto del crédito: ") )
Credito.duracion_periodo_meses = int( input("Ingrese la duración del periodo de gracia (meses): ") )
Credito.tasa_interes_anual = float( input("Ingrese la tasa de interés anual (%): ") )
Credito.plazo_amortizacion = int( input("Ingrese el plazo de amortización (meses): ") ) 
# Llamar al controlador para que inserte en la BD
ControladorCreditos.insertar( Credito )

print( "Credito insertado exitosamente!")