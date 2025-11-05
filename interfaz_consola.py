"""
Interfaz de consola para el sistema de gestión de créditos educativos
Cumple con los requerimientos de funcionalidad de Insertar, Modificar y Buscar datos
"""

import sys
import os

# Añadir rutas al path
here = os.path.dirname(__file__)
src_path = os.path.abspath(os.path.join(here, "src"))
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from model.credito import Credito
from controller.controlador_creditos import ControladorCreditos


def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*60)
    print("   SISTEMA DE GESTIÓN DE CRÉDITOS EDUCATIVOS")
    print("="*60)
    print("1. Insertar nuevo crédito")
    print("2. Buscar crédito")
    print("3. Modificar crédito")
    print("4. Eliminar crédito")
    print("5. Listar todos los créditos")
    print("6. Crear tablas (Inicialización)")
    print("0. Salir")
    print("="*60)


def insertar_credito():
    """Funcionalidad para insertar un nuevo crédito"""
    print("\n--- INSERTAR NUEVO CRÉDITO ---")
    try:
        nombre = input("Nombre del beneficiario: ").strip()
        if not nombre:
            print("❌ Error: El nombre no puede estar vacío")
            return
        
        monto = input("Monto del crédito (en pesos): ")
        duracion = input("Duración en meses: ")
        tasa = input("Tasa de interés anual (%): ")
        plazo = input("Plazo de amortización (meses): ")
        
        credito = Credito(
            nombre=nombre,
            monto_credito=int(monto),
            duracion_periodo_meses=int(duracion),
            tasa_interes_anual=float(tasa),
            plazo_amortizacion=int(plazo)
        )
        
        ControladorCreditos.insertar(credito)
        print(f"✅ Crédito para '{nombre}' insertado exitosamente!")
        
    except ValueError as e:
        print(f"❌ Error: Datos inválidos. {e}")
    except Exception as e:
        print(f"❌ Error al insertar: {e}")


def buscar_credito():
    """Funcionalidad para buscar un crédito"""
    print("\n--- BUSCAR CRÉDITO ---")
    try:
        nombre = input("Nombre del beneficiario a buscar: ").strip()
        if not nombre:
            print("❌ Error: El nombre no puede estar vacío")
            return
        
        credito = ControladorCreditos.buscar_credito(nombre)
        
        if credito:
            print("\n✅ Crédito encontrado:")
            print(f"  Nombre: {credito.nombre}")
            print(f"  Monto: ${credito.monto_credito:,}")
            print(f"  Duración: {credito.duracion_periodo_meses} meses")
            print(f"  Tasa de interés: {credito.tasa_interes_anual}%")
            print(f"  Plazo amortización: {credito.plazo_amortizacion} meses")
        else:
            print(f"❌ No se encontró ningún crédito para '{nombre}'")
            
    except Exception as e:
        print(f"❌ Error al buscar: {e}")


def modificar_credito():
    """Funcionalidad para modificar un crédito existente"""
    print("\n--- MODIFICAR CRÉDITO ---")
    try:
        nombre = input("Nombre del beneficiario a modificar: ").strip()
        if not nombre:
            print("❌ Error: El nombre no puede estar vacío")
            return
        
        # Verificar que existe
        credito_existente = ControladorCreditos.buscar_credito(nombre)
        if not credito_existente:
            print(f"❌ No se encontró ningún crédito para '{nombre}'")
            return
        
        print("\n📋 Datos actuales:")
        print(f"  Monto: ${credito_existente.monto_credito:,}")
        print(f"  Duración: {credito_existente.duracion_periodo_meses} meses")
        print(f"  Tasa: {credito_existente.tasa_interes_anual}%")
        print(f"  Plazo: {credito_existente.plazo_amortizacion} meses")
        
        print("\n🔄 Ingrese los nuevos datos:")
        monto = input(f"Nuevo monto [{credito_existente.monto_credito}]: ") or credito_existente.monto_credito
        duracion = input(f"Nueva duración [{credito_existente.duracion_periodo_meses}]: ") or credito_existente.duracion_periodo_meses
        tasa = input(f"Nueva tasa [{credito_existente.tasa_interes_anual}]: ") or credito_existente.tasa_interes_anual
        plazo = input(f"Nuevo plazo [{credito_existente.plazo_amortizacion}]: ") or credito_existente.plazo_amortizacion
        
        credito_actualizado = Credito(
            nombre=nombre,
            monto_credito=int(monto),
            duracion_periodo_meses=int(duracion),
            tasa_interes_anual=float(tasa),
            plazo_amortizacion=int(plazo)
        )
        
        if ControladorCreditos.actualizar(credito_actualizado):
            print(f"✅ Crédito de '{nombre}' actualizado exitosamente!")
        else:
            print(f"❌ No se pudo actualizar el crédito")
            
    except ValueError as e:
        print(f"❌ Error: Datos inválidos. {e}")
    except Exception as e:
        print(f"❌ Error al modificar: {e}")


def eliminar_credito():
    """Funcionalidad para eliminar un crédito"""
    print("\n--- ELIMINAR CRÉDITO ---")
    try:
        nombre = input("Nombre del beneficiario a eliminar: ").strip()
        if not nombre:
            print("❌ Error: El nombre no puede estar vacío")
            return
        
        # Verificar que existe
        credito = ControladorCreditos.buscar_credito(nombre)
        if not credito:
            print(f"❌ No se encontró ningún crédito para '{nombre}'")
            return
        
        confirmacion = input(f"⚠️  ¿Está seguro de eliminar el crédito de '{nombre}'? (s/n): ")
        if confirmacion.lower() == 's':
            if ControladorCreditos.eliminar(nombre):
                print(f"✅ Crédito de '{nombre}' eliminado exitosamente!")
            else:
                print(f"❌ No se pudo eliminar el crédito")
        else:
            print("❌ Operación cancelada")
            
    except Exception as e:
        print(f"❌ Error al eliminar: {e}")


def listar_creditos():
    """Funcionalidad para listar todos los créditos"""
    print("\n--- LISTA DE TODOS LOS CRÉDITOS ---")
    try:
        creditos = ControladorCreditos.listar_todos()
        
        if not creditos:
            print("📭 No hay créditos registrados en la base de datos")
            return
        
        print(f"\n📊 Total de créditos: {len(creditos)}\n")
        for i, credito in enumerate(creditos, 1):
            print(f"{i}. {credito.nombre}")
            print(f"   Monto: ${credito.monto_credito:,}")
            print(f"   Duración: {credito.duracion_periodo_meses} meses | Tasa: {credito.tasa_interes_anual}% | Plazo: {credito.plazo_amortizacion} meses")
            print()
            
    except Exception as e:
        print(f"❌ Error al listar: {e}")


def inicializar_tablas():
    """Crear las tablas en la base de datos"""
    print("\n--- INICIALIZAR BASE DE DATOS ---")
    try:
        confirmacion = input("⚠️  Esto creará las tablas necesarias. ¿Continuar? (s/n): ")
        if confirmacion.lower() == 's':
            ControladorCreditos.crear_tablas()
            print("✅ Tablas creadas exitosamente!")
        else:
            print("❌ Operación cancelada")
    except Exception as e:
        print(f"❌ Error al crear tablas: {e}")


def main():
    """Función principal del programa"""
    print("\n🎓 Bienvenido al Sistema de Gestión de Créditos Educativos")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("\nSeleccione una opción: ").strip()
            
            if opcion == "1":
                insertar_credito()
            elif opcion == "2":
                buscar_credito()
            elif opcion == "3":
                modificar_credito()
            elif opcion == "4":
                eliminar_credito()
            elif opcion == "5":
                listar_creditos()
            elif opcion == "6":
                inicializar_tablas()
            elif opcion == "0":
                print("\n👋 ¡Hasta luego!")
                break
            else:
                print("❌ Opción inválida. Por favor, seleccione una opción del menú.")
                
        except KeyboardInterrupt:
            print("\n\n👋 ¡Hasta luego!")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")


if __name__ == "__main__":
    main()
