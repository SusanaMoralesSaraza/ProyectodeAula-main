"""
Aplicación Web Flask para Gestión de Créditos Educativos
Sistema completo con funcionalidades CRUD y interfaz web
"""

from flask import Flask, render_template, request, redirect, url_for, flash
import sys
import os

# Añadir rutas al path
here = os.path.dirname(__file__)
src_path = os.path.abspath(os.path.join(here, "src"))
if src_path not in sys.path:
    sys.path.insert(0, src_path)
if here not in sys.path:
    sys.path.insert(0, here)

from model.credito import Credito
from controller.controlador_creditos import ControladorCreditos

# Flask constructor
app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui_cambiar_en_produccion'


# ==================== RUTA PRINCIPAL ====================
@app.route('/')
def index():
    """Menú principal de la aplicación"""
    return render_template('index.html')


# ==================== CREAR TABLAS ====================
@app.route('/crear_tablas', methods=['GET', 'POST'])
def crear_tablas():
    """Opción para crear las tablas de la BD"""
    if request.method == 'POST':
        try:
            ControladorCreditos.crear_tablas()
            flash('✅ Tablas creadas exitosamente!', 'success')
        except Exception as e:
            flash(f'❌ Error al crear tablas: {str(e)}', 'error')
        return redirect(url_for('index'))
    return render_template('crear_tablas.html')


# ==================== LISTAR CRÉDITOS ====================
@app.route('/creditos')
def listar_creditos():
    """Funcionalidad Web principal - Lista todos los créditos"""
    try:
        creditos = ControladorCreditos.listar_todos()
        return render_template('listar_creditos.html', creditos=creditos)
    except Exception as e:
        flash(f'❌ Error al listar créditos: {str(e)}', 'error')
        return redirect(url_for('index'))


# ==================== BUSCAR CRÉDITO ====================
@app.route('/buscar', methods=['GET', 'POST'])
def buscar_credito():
    """Funcionalidad Web para Buscar"""
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        if not nombre:
            flash('⚠️ Por favor ingrese un nombre para buscar', 'warning')
            return render_template('buscar_credito.html')
        
        try:
            credito = ControladorCreditos.buscar_credito(nombre)
            if credito:
                return render_template('buscar_credito.html', credito=credito, buscado=True)
            else:
                flash(f'❌ No se encontró ningún crédito para "{nombre}"', 'error')
                return render_template('buscar_credito.html', buscado=True)
        except Exception as e:
            flash(f'❌ Error al buscar: {str(e)}', 'error')
            return render_template('buscar_credito.html')
    
    return render_template('buscar_credito.html', buscado=False)


# ==================== INSERTAR CRÉDITO ====================
@app.route('/insertar', methods=['GET', 'POST'])
def insertar_credito():
    """Funcionalidad Web para Insertar"""
    if request.method == 'POST':
        try:
            nombre = request.form.get('nombre', '').strip()
            monto_credito = request.form.get('monto_credito', '').strip()
            duracion_periodo_meses = request.form.get('duracion_periodo_meses', '').strip()
            tasa_interes_anual = request.form.get('tasa_interes_anual', '').strip()
            plazo_amortizacion = request.form.get('plazo_amortizacion', '').strip()
            
            # Validaciones
            if not all([nombre, monto_credito, duracion_periodo_meses, tasa_interes_anual, plazo_amortizacion]):
                flash('⚠️ Todos los campos son obligatorios', 'warning')
                return render_template('insertar_credito.html')
            
            # Crear objeto crédito
            credito = Credito(
                nombre=nombre,
                monto_credito=int(monto_credito),
                duracion_periodo_meses=int(duracion_periodo_meses),
                tasa_interes_anual=float(tasa_interes_anual),
                plazo_amortizacion=int(plazo_amortizacion)
            )
            
            # Insertar en BD
            ControladorCreditos.insertar(credito)
            flash(f'✅ Crédito para "{nombre}" insertado exitosamente!', 'success')
            return redirect(url_for('listar_creditos'))
            
        except ValueError as e:
            flash(f'❌ Error: Datos inválidos. Verifique los valores numéricos.', 'error')
            return render_template('insertar_credito.html')
        except Exception as e:
            flash(f'❌ Error al insertar: {str(e)}', 'error')
            return render_template('insertar_credito.html')
    
    return render_template('insertar_credito.html')


# ==================== MODIFICAR CRÉDITO ====================
@app.route('/modificar', methods=['GET', 'POST'])
def modificar_credito():
    """Funcionalidad Web para Modificar"""
    if request.method == 'POST':
        # Si es búsqueda para modificar
        if 'buscar' in request.form:
            nombre = request.form.get('nombre', '').strip()
            if not nombre:
                flash('⚠️ Por favor ingrese un nombre para buscar', 'warning')
                return render_template('modificar_credito.html')
            
            try:
                credito = ControladorCreditos.buscar_credito(nombre)
                if credito:
                    return render_template('modificar_credito.html', credito=credito, encontrado=True)
                else:
                    flash(f'❌ No se encontró ningún crédito para "{nombre}"', 'error')
                    return render_template('modificar_credito.html')
            except Exception as e:
                flash(f'❌ Error al buscar: {str(e)}', 'error')
                return render_template('modificar_credito.html')
        
        # Si es actualización
        elif 'actualizar' in request.form:
            try:
                nombre = request.form.get('nombre', '').strip()
                monto_credito = request.form.get('monto_credito', '').strip()
                duracion_periodo_meses = request.form.get('duracion_periodo_meses', '').strip()
                tasa_interes_anual = request.form.get('tasa_interes_anual', '').strip()
                plazo_amortizacion = request.form.get('plazo_amortizacion', '').strip()
                
                if not all([nombre, monto_credito, duracion_periodo_meses, tasa_interes_anual, plazo_amortizacion]):
                    flash('⚠️ Todos los campos son obligatorios', 'warning')
                    return redirect(url_for('modificar_credito'))
                
                credito = Credito(
                    nombre=nombre,
                    monto_credito=int(monto_credito),
                    duracion_periodo_meses=int(duracion_periodo_meses),
                    tasa_interes_anual=float(tasa_interes_anual),
                    plazo_amortizacion=int(plazo_amortizacion)
                )
                
                if ControladorCreditos.actualizar(credito):
                    flash(f'✅ Crédito de "{nombre}" actualizado exitosamente!', 'success')
                    return redirect(url_for('listar_creditos'))
                else:
                    flash(f'❌ No se pudo actualizar el crédito', 'error')
                    return redirect(url_for('modificar_credito'))
                    
            except ValueError:
                flash(f'❌ Error: Datos inválidos. Verifique los valores numéricos.', 'error')
                return redirect(url_for('modificar_credito'))
            except Exception as e:
                flash(f'❌ Error al modificar: {str(e)}', 'error')
                return redirect(url_for('modificar_credito'))
    
    return render_template('modificar_credito.html', encontrado=False)


# ==================== ELIMINAR CRÉDITO ====================
@app.route('/eliminar/<nombre>', methods=['POST'])
def eliminar_credito(nombre):
    """Eliminar un crédito"""
    try:
        if ControladorCreditos.eliminar(nombre):
            flash(f'✅ Crédito de "{nombre}" eliminado exitosamente!', 'success')
        else:
            flash(f'❌ No se pudo eliminar el crédito', 'error')
    except Exception as e:
        flash(f'❌ Error al eliminar: {str(e)}', 'error')
    
    return redirect(url_for('listar_creditos'))


# ==================== MANEJO DE ERRORES ====================
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


# ==================== EJECUTAR APLICACIÓN ====================
if __name__ == '__main__':
    # Para desarrollo local
    app.run(debug=True, host='0.0.0.0', port=5000)

