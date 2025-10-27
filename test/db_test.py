import sys
sys.path.append("src")  # Agrega el directorio padre al path para importar src
from src.model.credito import Credito

from src.controller.controlador_creditos import ControladorCreditos

import unittest

class TetsDBCredito(unittest.TestCase):

    def test_insertar(self):
        #Crear una instancia la calse credito
        credito_prueba = Credito(nombre="Felipe", monto_credito = "25000000", duracion_periodo_meses = "72",
                                  tasa_interes_anual= "12", plazo_amortizacion = "140")
        
        #Insertar en la base de datos
        ControladorCreditos.Insertar(credito_prueba)

        #Buscar
        encontrado = ControladorCreditos.Buscar("Felipe")

        #Comparar si es igual la buscada con la inicial 
        credito_prueba.is_equal(encontrado)
        
    def buscar(self):
        pass