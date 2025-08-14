from monto import conversion_tasa_anual, calcular_valor_a_pagar

import monto

import unittest


class pruebas_credito(unittest.TestCase):

    def test_normal_1(self):
        #entradas
        monto_credito = 20000000
        duracion_periodo_meses = 48
        tasa_interes_anual = 12
        plazo_amortizacion = 120

        #probar proceso de conversion
        _, _, _, total = conversion_tasa_anual(monto_credito, duracion_periodo_meses, tasa_interes_anual, plazo_amortizacion)
        self.assertEqual(round(total, 2), 32244521.55)

    def test_normal_2(self):
        #entradas
        monto_credito = 22000000
        duracion_periodo_meses = 60
        tasa_interes_anual = 12
        plazo_amortizacion = 130

        #probar proceso de conversion
        _, _, _, total = conversion_tasa_anual(monto_credito, duracion_periodo_meses, tasa_interes_anual, plazo_amortizacion)    
        self.assertEqual(round(total, 2), 39967327.37)

    def test_normal_3(self):
        #entradas
        monto_credito = 25000000
        duracion_periodo_meses = 72
        tasa_interes_anual = 12
        plazo_amortizacion = 140

        #probar proceso de conversion
        _, _, _, total = conversion_tasa_anual(monto_credito, duracion_periodo_meses, tasa_interes_anual, plazo_amortizacion)
        self.assertEqual(round(total, 2), 51177482.8)

    def test_extraordinary_1(self):
        #entradas
        monto_credito = 15000000
        duracion_periodo_meses = 36
        tasa_interes_anual = 10
        plazo_amortizacion = 180

        #probar proceso de conversion
        _, _, _, total = conversion_tasa_anual(monto_credito, duracion_periodo_meses, tasa_interes_anual, plazo_amortizacion)
        self.assertEqual(round(total, 2), 20222727.64)

    def test_extraordinary_2(self):
        #entradas
        monto_credito = 25000000
        duracion_periodo_meses = 60
        tasa_interes_anual = 15
        plazo_amortizacion = 120

        #probar proceso de conversion
        _, _, _, total = conversion_tasa_anual(monto_credito, duracion_periodo_meses, tasa_interes_anual, plazo_amortizacion)
        self.assertEqual(round(total, 2), 52679533.67)

    def test_extraordinary_3(self):
        #entradas
        monto_credito = 25000000
        duracion_periodo_meses = 60
        tasa_interes_anual = 15
        plazo_amortizacion = 180

        #probar proceso de conversion
        _, _, _, total = conversion_tasa_anual(monto_credito, duracion_periodo_meses, tasa_interes_anual, plazo_amortizacion)
        self.assertEqual(round(total, 2), 52679533.67)

    def test_error_monto(self):
        #Entradas
        monto_credito = 0
        duracion_periodo_meses = 60
        tasa_interes_anual = 15
        plazo_amortizacion = 180

        #Proceso 
        with self.assertRaises(monto.ErrorMonto):
            monto.calcular_valor_a_pagar(monto_credito, tasa_interes_anual, duracion_periodo_meses, plazo_amortizacion)

    def test_error_periodo(self):
        #Entradas
        monto_credito = 25000000
        duracion_periodo_meses = 0
        tasa_interes_anual = 10
        plazo_amortizacion = 180

        #Proceso 
        with self.assertRaises(monto.ErrorPeriodoGracia):
            monto.calcular_valor_a_pagar(monto_credito, tasa_interes_anual, duracion_periodo_meses, plazo_amortizacion)

    def test_demasiadas_cuotas(self):
        #Entradas
        monto_credito = 20000000
        duracion_periodo_meses = 36
        tasa_interes_anual = 72
        plazo_amortizacion = 600

        #Proceso 
        with self.assertRaises(monto.ErrorPeriodoGracia):
            monto.calcular_valor_a_pagar(monto_credito, tasa_interes_anual, duracion_periodo_meses, plazo_amortizacion)
if __name__ == '__main__':
    unittest.main()

