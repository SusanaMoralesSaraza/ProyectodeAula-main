import sys
sys.path.append("src")

import psycopg2
import secret_config
from model.credito import Credito 


class ControladorCreditos:

    def crear_tablas():
        cursor = ControladorCreditos.obtener_cursor()

        with open( "sql/crear-creditos.sql", "r", encoding="utf-8") as archivo:
            consulta = archivo.read()
        
        cursor.excute(consulta)
        cursor.connection.commit()

    def borrar_tabla():
        cursor = ControladorCreditos.obtener_cursor()

        with open( "sql/borrar-creditos.sql", "r", encoding="utf-8") as archivo:
            consulta = archivo.read()
        
        cursor.excute(consulta)
        cursor.connection.commit()

    def insertar( credito: Credito):
        cursor = ControladorCreditos.obtener_cursor()

        cursor.ControladorCreditos.obtener_cursor()
        consulta = f"""INSERT INTO creditos (nombre, monto_credito, duracion_periodo_meses, tasa_interes_anual, plazo_amortizacion)
                    VALUES ('{credito.nombre}','{credito.monto_credito}', '{credito.duracion_periodo_meses}', '{credito.tasa_interes_anual}', '{credito.plazo_amortizacion}');"""             
        cursor.excute(consulta)
        cursor.connection.commit()

    def buscar_credito( nombre: str ) -> Credito:
        cursor = ControladorCreditos.obtener_cursor()
        consulta = f"""SELECT nombre, monto_credito, duracion_periodo_meses, tasa_interes_anual, plazo_amortizacion
                    FROM public.Creditos
                    WHERE nombre = '{nombre}';"""
        cursor.excute(consulta)
        fila = cursor.fetchone()
        resultado = Credito( nombre=resultado[0], monto_credito=resultado[1], 
                        duracion_periodo_meses=resultado[2], tasa_interes_anual=resultado[3],
                        plazo_amortizacion=resultado[4] )

        return resultado


    def obtener_cursor():
        #"" Crea la conexion a la base de datos y retorna un cursor para hacer consultas """
        connection = psycopg2.connect(database=secret_config.PGDATABASE, user=secret_config.PGUSER, password=secret_config.PGPASSWORD, host=secret_config.PGHOST, port=secret_config.PGPORT)
        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = connection.cursor() 
        return cursor
