class Credito:
    def __init__(self, nombre: str = None,
                 monto_credito = None,
                 duracion_periodo_meses = None,
                 tasa_interes_anual = None,
                 plazo_amortizacion = None):
        self.nombre = nombre
        self.monto_credito = monto_credito
        self.duracion_periodo_meses = duracion_periodo_meses
        self.tasa_interes_anual = tasa_interes_anual
        self.plazo_amortizacion = plazo_amortizacion

    def is_equal(self: 'Credito', otro: 'Credito') -> bool:
        assert (self.nombre == otro.nombre)
        assert (self.monto_credito == otro.monto_credito)
        assert (self.duracion_periodo_meses == otro.duracion_periodo_meses)
        assert (self.tasa_interes_anual == otro.tasa_interes_anual)
        assert (self.plazo_amortizacion == otro.plazo_amortizacion)
        return True

        