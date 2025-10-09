import sys
sys.path.append("src")

import psycopg2

from model.credito import Credito 



class ControladorCreditos():

    def Insertar( credito: Credito):
        conexion = psycopg2.connect(database="credit_card_l086", user="profesor", password="xUchqyFss00mMhMlA7LdINjxAdb0FAwy", host="dpg-d3dvosvdiees73fo2jm0-a", port="5432")
        cursor = conexion.cursor()
        sql = f"""INSERT INTO creditos (monto_credito, duracion_periodo_meses, tasa_interes_anual, plazo_amortizacion)
                VALUES ('{credito.monto_credito}', '{credito.duracion_periodo_meses}', '{credito.tasa_interes_anual}', '{credito.plazo_amortizacion}');"""
        cursor.execute(sql)                 
        conexion.commit()

    def Buscar( duracion_periodo_meses: str ) -> Credito:
        pass