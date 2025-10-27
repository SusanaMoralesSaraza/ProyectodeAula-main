import sys
sys.path.append("src")

import psycopg2
from model.credito import Credito

# Parámetros de conexión (mantengo los valores que ya tenías)
DB_PARAMS = {
    "database": "credit_card_l086",
    "user": "profesor",
    "password": "xUchqyFss00mMhMlA7LdINjxAdb0FAwy",
    "host": "dpg-d3dvosvdiees73fo2jm0-a",
    "port": "5432",
}

def _get_connection():
    return psycopg2.connect(**DB_PARAMS)


class ControladorCreditos():

    def Insertar( credito: Credito):
        conn = _get_connection()
        try:
            with conn.cursor() as cursor:
                sql = """
                    INSERT INTO public.creditos
                    (nombre, monto_credito, duracion_periodo_meses, tasa_interes_anual, plazo_amortizacion)
                    VALUES (%s, %s, %s, %s, %s);
                """
                params = (
                    credito.nombre,
                    int(credito.monto_credito) if credito.monto_credito not in (None, "") else None,
                    int(credito.duracion_periodo_meses) if credito.duracion_periodo_meses not in (None, "") else None,
                    float(credito.tasa_interes_anual) if credito.tasa_interes_anual not in (None, "") else None,
                    int(credito.plazo_amortizacion) if credito.plazo_amortizacion not in (None, "") else None,
                )
                cursor.execute(sql, params)
            conn.commit()
        finally:
            try:
                conn.close()
            except Exception:
                pass

    def Buscar( nombre: str ) -> Credito:
        conn = _get_connection()
        try:
            with conn.cursor() as cursor:
                sql = """
                    SELECT nombre, monto_credito, duracion_periodo_meses, tasa_interes_anual, plazo_amortizacion
                    FROM public.creditos
                    WHERE nombre = %s;
                """
                cursor.execute(sql, (nombre,))
                resultado = cursor.fetchone()
            if not resultado:
                return None
            credito = Credito( nombre=resultado[0], monto_credito=resultado[1],
                               duracion_periodo_meses=resultado[2], tasa_interes_anual=resultado[3],
                               plazo_amortizacion=resultado[4] )
            return credito
        finally:
            try:
                conn.close()
            except Exception:
                pass

    def Eliminar( nombre: str ) -> bool:
        """
        Borra la fila cuyo nombre coincida. Devuelve True si se borró al menos una fila.
        """
        conn = _get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM public.creditos WHERE nombre = %s;", (nombre,))
                deleted = cursor.rowcount
            conn.commit()
            return deleted > 0
        finally:
            try:
                conn.close()
            except Exception:
                pass