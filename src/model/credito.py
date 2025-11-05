class Credito:
    """Modelo ORM para la tabla creditos"""
    
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

    def is_equal(self, otro: 'Credito') -> bool:
        """Compara si dos objetos Credito son iguales"""
        if otro is None:
            return False
        return (
            str(self.nombre) == str(otro.nombre) and
            str(self.monto_credito) == str(otro.monto_credito) and
            str(self.duracion_periodo_meses) == str(otro.duracion_periodo_meses) and
            str(self.tasa_interes_anual) == str(otro.tasa_interes_anual) and
            str(self.plazo_amortizacion) == str(otro.plazo_amortizacion)
        )
    
    def __str__(self):
        """Representación en string del crédito"""
        return f"Credito(nombre={self.nombre}, monto={self.monto_credito}, duracion={self.duracion_periodo_meses}, tasa={self.tasa_interes_anual}, plazo={self.plazo_amortizacion})"
    
    def __repr__(self):
        return self.__str__()

        