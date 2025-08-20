import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from model import monto
from model.monto import conversion_tasa_anual, calcular_valor_a_pagar
import unittest


class pruebas_credito(unittest.TestCase):

    # Casos normales
    def test_normal_1(self):
        _, _, _, total, _ = conversion_tasa_anual(20000000, 48, 12, 120)
        self.assertAlmostEqual(total, 55513825.06, places=2)

    def test_normal_2(self):
        _, _, _, total, _ = conversion_tasa_anual(22000000, 60, 12, 130)
        self.assertAlmostEqual(total, 71596150.81, places=2)

    def test_normal_3(self):
        _, _, _, total, _ = conversion_tasa_anual(25000000, 72, 12, 140)
        self.assertAlmostEqual(total, 95317497.25, places=2)

    # Casos extraordinarios
    def test_extraordinary_1(self):
        _, _, _, total, _ = conversion_tasa_anual(15000000, 36, 10, 180)
        self.assertAlmostEqual(total, 39116603.9, places=2)

    def test_extraordinary_2(self):
        _, _, _, total, _ = conversion_tasa_anual(25000000, 60, 15, 120)
        self.assertAlmostEqual(total, 101988603.65, places=2)

    def test_extraordinary_3(self):
        _, _, _, total, _ = conversion_tasa_anual(25000000, 60, 15, 180)
        self.assertAlmostEqual(total, 132713274.15, places=2)

    # Casos de error
    def test_error_monto(self):
        with self.assertRaises(monto.ErrorMonto):
            calcular_valor_a_pagar(0, 15, 60, 180)

    def test_error_periodo(self):
        with self.assertRaises(monto.ErrorPeriodoGracia):
            calcular_valor_a_pagar(25000000, 10, 0, 180)

    def test_error_demasiadas_cuotas(self):
        with self.assertRaises(monto.ErrorDemasiadasCuotas):
            calcular_valor_a_pagar(20000000, 72, 36, 600)

    def test_error_tasa_negativa(self):
        with self.assertRaises(ValueError):
            conversion_tasa_anual(20000000, 36, -5, 120)

    def test_error_plazo_pequeno(self):
        with self.assertRaises(monto.ErrorDemasiadasCuotas):
            calcular_valor_a_pagar(20000000, 12, 24, 100)

if __name__ == '__main__':
    unittest.main()
