import sys
import os

# Añadir rutas al path
here = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(here, "..", ".."))
src_path = os.path.join(project_root, "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import psycopg2
from typing import Optional
from model.credito import Credito

# Importar secret_config
try:
    import secret_config as _sc
    DB_PARAMS = {
        "database": _sc.PGDATABASE,
        "user": _sc.PGUSER,
        "password": _sc.PGPASSWORD,
        "host": _sc.PGHOST,
        "port": _sc.PGPORT,
    }
except Exception:
    DB_PARAMS = {
        "database": os.getenv("DB_NAME", "credit_educativo"),
        "user": os.getenv("DB_USER", "susana"),
        "password": os.getenv("DB_PASS", ""),
        "host": os.getenv("DB_HOST", "localhost"),
        "port": os.getenv("DB_PORT", "5432"),
    }


def obtener_cursor():
    """Crea la conexión a la base de datos y retorna un cursor para hacer consultas"""
    connection = psycopg2.connect(**DB_PARAMS)
    cursor = connection.cursor()
    return cursor


class ControladorCreditos:
    """Controlador para operaciones CRUD en la tabla creditos"""

    @staticmethod
    def crear_tablas():
        """Crea la tabla creditos si no existe"""
        cursor = obtener_cursor()
        try:
            ruta_sql = os.path.join(project_root, "sql", "crear-creditos.sql")
            if os.path.exists(ruta_sql):
                with open(ruta_sql, "r", encoding="utf-8") as archivo:
                    consulta = archivo.read()
            else:
                consulta = """
                CREATE TABLE IF NOT EXISTS public.creditos (
                    nombre VARCHAR(100) PRIMARY KEY,
                    monto_credito INTEGER NOT NULL,
                    duracion_periodo_meses INTEGER NOT NULL,
                    tasa_interes_anual DECIMAL(5,2) NOT NULL,
                    plazo_amortizacion INTEGER NOT NULL
                );
                """
            cursor.execute(consulta)
            cursor.connection.commit()
        finally:
            cursor.connection.close()

    @staticmethod
    def borrar_tabla():
        """Elimina la tabla creditos si existe"""
        cursor = obtener_cursor()
        try:
            ruta_sql = os.path.join(project_root, "sql", "borrar-creditos.sql")
            if os.path.exists(ruta_sql):
                with open(ruta_sql, "r", encoding="utf-8") as archivo:
                    consulta = archivo.read()
            else:
                consulta = "DROP TABLE IF EXISTS public.creditos CASCADE;"
            cursor.execute(consulta)
            cursor.connection.commit()
        finally:
            cursor.connection.close()

    @staticmethod
    def insertar(credito: Credito):
        """Inserta un nuevo crédito en la base de datos"""
        cursor = obtener_cursor()
        try:
            consulta = """
                INSERT INTO public.creditos 
                (nombre, monto_credito, duracion_periodo_meses, tasa_interes_anual, plazo_amortizacion)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (nombre) DO UPDATE
                SET monto_credito = EXCLUDED.monto_credito,
                    duracion_periodo_meses = EXCLUDED.duracion_periodo_meses,
                    tasa_interes_anual = EXCLUDED.tasa_interes_anual,
                    plazo_amortizacion = EXCLUDED.plazo_amortizacion;
            """
            cursor.execute(consulta, (
                credito.nombre,
                int(credito.monto_credito),
                int(credito.duracion_periodo_meses),
                float(credito.tasa_interes_anual),
                int(credito.plazo_amortizacion)
            ))
            cursor.connection.commit()
        finally:
            cursor.connection.close()

    @staticmethod
    def buscar_credito(nombre: str) -> Optional[Credito]:
        """Busca un crédito por nombre"""
        cursor = obtener_cursor()
        try:
            consulta = """
                SELECT nombre, monto_credito, duracion_periodo_meses, tasa_interes_anual, plazo_amortizacion
                FROM public.creditos
                WHERE nombre = %s;
            """
            cursor.execute(consulta, (nombre,))
            fila = cursor.fetchone()
            if not fila:
                return None
            return Credito(
                nombre=fila[0],
                monto_credito=fila[1],
                duracion_periodo_meses=fila[2],
                tasa_interes_anual=fila[3],
                plazo_amortizacion=fila[4]
            )
        finally:
            cursor.connection.close()

    @staticmethod
    def actualizar(credito: Credito):
        """Actualiza un crédito existente en la base de datos"""
        cursor = obtener_cursor()
        try:
            consulta = """
                UPDATE public.creditos
                SET monto_credito = %s,
                    duracion_periodo_meses = %s,
                    tasa_interes_anual = %s,
                    plazo_amortizacion = %s
                WHERE nombre = %s;
            """
            cursor.execute(consulta, (
                int(credito.monto_credito),
                int(credito.duracion_periodo_meses),
                float(credito.tasa_interes_anual),
                int(credito.plazo_amortizacion),
                credito.nombre
            ))
            cursor.connection.commit()
            return cursor.rowcount > 0
        finally:
            cursor.connection.close()

    @staticmethod
    def eliminar(nombre: str) -> bool:
        """Elimina un crédito por nombre"""
        cursor = obtener_cursor()
        try:
            consulta = "DELETE FROM public.creditos WHERE nombre = %s;"
            cursor.execute(consulta, (nombre,))
            cursor.connection.commit()
            return cursor.rowcount > 0
        finally:
            cursor.connection.close()

    @staticmethod
    def listar_todos():
        """Lista todos los créditos en la base de datos"""
        cursor = obtener_cursor()
        try:
            consulta = """
                SELECT nombre, monto_credito, duracion_periodo_meses, tasa_interes_anual, plazo_amortizacion
                FROM public.creditos
                ORDER BY nombre;
            """
            cursor.execute(consulta)
            filas = cursor.fetchall()
            creditos = []
            for fila in filas:
                creditos.append(Credito(
                    nombre=fila[0],
                    monto_credito=fila[1],
                    duracion_periodo_meses=fila[2],
                    tasa_interes_anual=fila[3],
                    plazo_amortizacion=fila[4]
                ))
            return creditos
        finally:
            cursor.connection.close()
