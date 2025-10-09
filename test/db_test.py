import sys
sys.path.append("src")  # Agrega el directorio padre al path para importar src
from src.model.credito import Credito

from src.controller.controlador_creditos import ControladorCreditos

import unittest

class TetsDBCredito(unittest.TestCase):

    def test_insertar_y_buscar(self):
        credito_prueba = Credito(monto_credito = "20000000", duracion_periodo_meses = "48",
                                  tasa_interes_anual= "12", plazo_amortizacion = "120")
        
        #Pedir al controlador que inserte el credito
        ControladorCreditos.Insertar(credito_prueba)

        #Pedir al controlador que busque el credito
        duracion_periodo_meses = ControladorCreditos.Buscar("48")

        #Verificar que el credito encontrado es igual al que se inserto
        self.assertTrue( credito_prueba.is_equal(duracion_periodo_meses) )