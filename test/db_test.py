import sys
sys.path.append("src")  # Agrega el directorio padre al path para importar src
from src.model.credito import Credito

from src.controller.controlador_creditos import ControladorCreditos

import unittest

class TetsDBCredito(unittest.TestCase):

    def test_insertar_y_buscar(self):
        credito_prueba = Credito(nombre="Felipe", monto_credito = "25000000", duracion_periodo_meses = "72",
                                  tasa_interes_anual= "12", plazo_amortizacion = "140")
        
        #Pedir al controlador que inserte el credito
        ControladorCreditos.Insertar(credito_prueba)

        #Pedir al controlador que busque el credito
        encontrado = ControladorCreditos.Buscar("Felipe")

        #Verificar que el credito encontrado es igual al que se inserto
        self.assertTrue( credito_prueba.is_equal(encontrado) )

    def buscar(self):
        pass