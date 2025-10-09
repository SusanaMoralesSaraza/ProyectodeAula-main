class Credito:
    def __init__(self, monto_credito,
duracion_periodo_meses,
tasa_interes_anual,
plazo_amortizacion):
        self.monto_credito = monto_credito
        self.duracion_periodo_meses = duracion_periodo_meses
        self.tasa_interes_anual = tasa_interes_anual
        self.plazo_amortizacion = plazo_amortizacion


    def is_equal(self, otro):
        return (
            self.monto_credito == otro.monto_credito and
            self.duracion_periodo_meses == otro.duracion_periodo_meses and
            self.tasa_interes_anual == otro.tasa_interes_anual and
            self.plazo_amortizacion == otro.plazo_amortizacion
        )