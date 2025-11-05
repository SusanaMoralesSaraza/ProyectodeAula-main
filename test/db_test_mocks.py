"""
Tests con mocks - No requieren conexión a base de datos
Estos tests pueden ejecutarse localmente sin problemas de red
"""

import sys
import os
import unittest
from unittest.mock import patch, MagicMock

# Añadir rutas al path
here = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(here, ".."))
src_path = os.path.join(project_root, "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from model.credito import Credito
from controller.controlador_creditos import ControladorCreditos


class TestDBCreditoConMocks(unittest.TestCase):
    """Tests para operaciones CRUD usando mocks (sin conexión real a BD)"""

    def setUp(self):
        """Se ejecuta antes de cada test"""
        self.patcher = patch('controller.controlador_creditos.obtener_cursor')
        self.mock_obtener_cursor = self.patcher.start()
        
        # Configurar mock de cursor
        self.mock_cursor = MagicMock()
        self.mock_connection = MagicMock()
        self.mock_cursor.connection = self.mock_connection
        self.mock_obtener_cursor.return_value = self.mock_cursor

    def tearDown(self):
        """Se ejecuta después de cada test"""
        self.patcher.stop()

    # ==================== TESTS DE INSERCIÓN (INSERT) ====================
    
    def test_01_insertar_credito_exitoso(self):
        """Caso normal: Insertar crédito válido"""
        credito = Credito(
            nombre="Felipe",
            monto_credito=25000000,
            duracion_periodo_meses=72,
            tasa_interes_anual=12,
            plazo_amortizacion=140
        )
        
        ControladorCreditos.insertar(credito)
        
        # Verificar que se llamó execute con los parámetros correctos
        self.mock_cursor.execute.assert_called_once()
        self.mock_connection.commit.assert_called_once()
        self.mock_connection.close.assert_called_once()

    def test_02_insertar_credito_exitoso_2(self):
        """Caso normal: Insertar segundo crédito válido"""
        credito = Credito(
            nombre="Maria",
            monto_credito=20000000,
            duracion_periodo_meses=60,
            tasa_interes_anual=12,
            plazo_amortizacion=120
        )
        
        ControladorCreditos.insertar(credito)
        
        self.mock_cursor.execute.assert_called_once()
        self.mock_connection.commit.assert_called_once()

    def test_03_insertar_credito_exitoso_3(self):
        """Caso normal: Insertar tercer crédito válido"""
        credito = Credito(
            nombre="Carlos",
            monto_credito=15000000,
            duracion_periodo_meses=48,
            tasa_interes_anual=10.5,
            plazo_amortizacion=100
        )
        
        ControladorCreditos.insertar(credito)
        
        self.mock_cursor.execute.assert_called_once()
        self.mock_connection.commit.assert_called_once()

    def test_04_insertar_credito_con_error_bd(self):
        """Caso de error: Simular error en la BD"""
        import psycopg2
        self.mock_cursor.execute.side_effect = psycopg2.Error("Error de BD")
        
        credito = Credito(
            nombre="TestError",
            monto_credito=10000000,
            duracion_periodo_meses=36,
            tasa_interes_anual=8,
            plazo_amortizacion=80
        )
        
        with self.assertRaises(psycopg2.Error):
            ControladorCreditos.insertar(credito)

    # ==================== TESTS DE ACTUALIZACIÓN (UPDATE) ====================

    def test_05_actualizar_credito_exitoso(self):
        """Caso normal: Actualizar crédito existente"""
        self.mock_cursor.rowcount = 1  # Simular que se actualizó 1 fila
        
        credito = Credito(
            nombre="Felipe",
            monto_credito=30000000,
            duracion_periodo_meses=84,
            tasa_interes_anual=11,
            plazo_amortizacion=150
        )
        
        resultado = ControladorCreditos.actualizar(credito)
        
        self.assertTrue(resultado)
        self.mock_cursor.execute.assert_called_once()
        self.mock_connection.commit.assert_called_once()

    def test_06_actualizar_credito_exitoso_2(self):
        """Caso normal: Actualizar segundo crédito"""
        self.mock_cursor.rowcount = 1
        
        credito = Credito(
            nombre="Maria",
            monto_credito=22000000,
            duracion_periodo_meses=66,
            tasa_interes_anual=11.5,
            plazo_amortizacion=130
        )
        
        resultado = ControladorCreditos.actualizar(credito)
        self.assertTrue(resultado)

    def test_07_actualizar_credito_exitoso_3(self):
        """Caso normal: Actualizar tercer crédito"""
        self.mock_cursor.rowcount = 1
        
        credito = Credito(
            nombre="Carlos",
            monto_credito=18000000,
            duracion_periodo_meses=54,
            tasa_interes_anual=11,
            plazo_amortizacion=110
        )
        
        resultado = ControladorCreditos.actualizar(credito)
        self.assertTrue(resultado)

    def test_08_actualizar_credito_inexistente(self):
        """Caso de error: Actualizar crédito que no existe"""
        self.mock_cursor.rowcount = 0  # No se actualizó ninguna fila
        
        credito = Credito(
            nombre="NoExiste",
            monto_credito=5000000,
            duracion_periodo_meses=24,
            tasa_interes_anual=7,
            plazo_amortizacion=50
        )
        
        resultado = ControladorCreditos.actualizar(credito)
        self.assertFalse(resultado)

    # ==================== TESTS DE CONSULTA (SELECT) ====================

    def test_09_buscar_credito_exitoso(self):
        """Caso normal: Buscar crédito existente"""
        # Simular que fetchone devuelve una fila
        self.mock_cursor.fetchone.return_value = ("Felipe", 25000000, 72, 12, 140)
        
        encontrado = ControladorCreditos.buscar_credito("Felipe")
        
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.nombre, "Felipe")
        self.assertEqual(encontrado.monto_credito, 25000000)

    def test_10_buscar_credito_exitoso_2(self):
        """Caso normal: Buscar segundo crédito existente"""
        self.mock_cursor.fetchone.return_value = ("Maria", 20000000, 60, 12, 120)
        
        encontrado = ControladorCreditos.buscar_credito("Maria")
        
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.nombre, "Maria")

    def test_11_buscar_credito_exitoso_3(self):
        """Caso normal: Buscar tercer crédito existente"""
        self.mock_cursor.fetchone.return_value = ("Carlos", 15000000, 48, 10.5, 100)
        
        encontrado = ControladorCreditos.buscar_credito("Carlos")
        
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.nombre, "Carlos")

    def test_12_buscar_credito_inexistente(self):
        """Caso de error: Buscar crédito que no existe"""
        self.mock_cursor.fetchone.return_value = None
        
        encontrado = ControladorCreditos.buscar_credito("UsuarioInexistente")
        
        self.assertIsNone(encontrado)

    # ==================== TESTS DE ELIMINACIÓN (DELETE) ====================

    def test_13_eliminar_credito_exitoso(self):
        """Caso normal: Eliminar crédito existente"""
        self.mock_cursor.rowcount = 1
        
        resultado = ControladorCreditos.eliminar("Felipe")
        
        self.assertTrue(resultado)
        self.mock_cursor.execute.assert_called_once()
        self.mock_connection.commit.assert_called_once()

    def test_14_eliminar_credito_exitoso_2(self):
        """Caso normal: Eliminar segundo crédito"""
        self.mock_cursor.rowcount = 1
        
        resultado = ControladorCreditos.eliminar("Carlos")
        
        self.assertTrue(resultado)

    def test_15_eliminar_credito_exitoso_3(self):
        """Caso normal: Eliminar tercer crédito"""
        self.mock_cursor.rowcount = 1
        
        resultado = ControladorCreditos.eliminar("Maria")
        
        self.assertTrue(resultado)

    def test_16_eliminar_credito_inexistente(self):
        """Caso de error: Eliminar crédito que no existe"""
        self.mock_cursor.rowcount = 0
        
        resultado = ControladorCreditos.eliminar("UsuarioInexistente")
        
        self.assertFalse(resultado)


if __name__ == '__main__':
    unittest.main(verbosity=2)
