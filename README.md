# 🎓 Sistema de Gestión de Créditos Educativos - Aplicación Web

## 📋 Descripción

Sistema web completo de gestión de créditos educativos desarrollado con Flask y PostgreSQL. Incluye todas las funcionalidades CRUD (Create, Read, Update, Delete) con interfaz web moderna y responsive.

---

## ✅ Funcionalidades Implementadas

### Funcionalidades Web Principales
- ✅ **Página Principal** - Menú de inicio con acceso a todas las funcionalidades
- ✅ **Listar Créditos** - Visualización de todos los créditos en tabla
- ✅ **Buscar Crédito** - Búsqueda por nombre de beneficiario
- ✅ **Insertar Crédito** - Formulario para agregar nuevos créditos
- ✅ **Modificar Crédito** - Actualización de créditos existentes
- ✅ **Eliminar Crédito** - Eliminación con confirmación
- ✅ **Crear Tablas BD** - Opción para inicializar la base de datos

### Características Técnicas
- ✅ Interfaz web moderna y responsive
- ✅ Validaciones de formularios
- ✅ Mensajes flash (éxito/error/advertencia)
- ✅ Manejo de errores (404, 500)
- ✅ Tests unitarios completos (16 tests)
- ✅ Consultas parametrizadas (seguridad)
- ✅ Arquitectura MVC limpia

---

## 🚀 Instalación y Ejecución Local

### Requisitos Previos
- Python 3.8 o superior
- PostgreSQL instalado o acceso a base de datos PostgreSQL en la nube

### Paso 1: Clonar el repositorio
```bash
git clone https://github.com/SusanaMoralesSaraza/ProyectodeAula-main.git
cd ProyectodeAula-main-1
```

### Paso 2: Crear entorno virtual (recomendado)
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Paso 3: Instalar dependencias
```bash
pip install -r requirements.txt
```

### Paso 4: Configurar la base de datos

Edita el archivo `secret_config.py` con tus credenciales de PostgreSQL:

```python
# Configuración de la base de datos PostgreSQL
PGHOST = 'tu-host.render.com'          # Host de tu BD
PGDATABASE = 'nombre_de_tu_bd'         # Nombre de la BD
PGUSER = 'tu_usuario'                  # Usuario
PGPASSWORD = 'tu_contraseña'           # Contraseña
PGPORT = '5432'                        # Puerto (generalmente 5432)
```

**Nota importante:** Si la base de datos está en blanco (nueva), debes crear las tablas.

### Paso 5: Crear las tablas en la base de datos

**Opción A - Desde la aplicación web:**
1. Ejecuta la aplicación (ver Paso 6)
2. Navega a: http://localhost:5000/crear_tablas
3. Haz clic en "Crear Tablas Ahora"

**Opción B - Desde Python:**
```python
python -c "from src.controller.controlador_creditos import ControladorCreditos; ControladorCreditos.crear_tablas(); print('Tablas creadas!')"
```

### Paso 6: Ejecutar la aplicación web
```bash
python app.py
```

La aplicación estará disponible en: **http://localhost:5000**

---

## 🧪 Ejecutar Tests Unitarios

El proyecto incluye 16 tests unitarios que cubren todas las operaciones CRUD:

```bash
# Ejecutar todos los tests
python -m unittest test.db_test -v
```

### Cobertura de Tests
- ✅ 4 tests INSERT (3 exitosos + 1 error)
- ✅ 4 tests UPDATE (3 exitosos + 1 error)
- ✅ 4 tests SELECT (3 exitosos + 1 error)
- ✅ 4 tests DELETE (3 exitosos + 1 error)

---

## 🌐 Despliegue en la Web (Render)

### Pasos para Despliegue

1. **Sube tu código a GitHub:**
   ```bash
   git add .
   git commit -m "Aplicación web completa"
   git push origin main
   ```

2. **Crea una base de datos PostgreSQL en Render:**
   - Dashboard → New → PostgreSQL
   - Copia las credenciales y actualiza `secret_config.py`

3. **Crea un Web Service en Render:**
   - Dashboard → New → Web Service
   - Conecta tu repositorio
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

4. **Crear las tablas:**
   - Visita: `https://tu-app.onrender.com/crear_tablas`

---

## 📁 Estructura del Proyecto

```
ProyectodeAula-main-1/
├── app.py                      # Aplicación Flask principal
├── requirements.txt            # Dependencias
├── Procfile                    # Para deployment
├── secret_config.py            # Configuración BD
│
├── src/
│   ├── model/
│   │   └── credito.py         # Modelo ORM
│   └── controller/
│       └── controlador_creditos.py  # Controlador CRUD
│
├── templates/                  # Plantillas HTML
│   ├── base.html
│   ├── index.html
│   ├── listar_creditos.html
│   ├── insertar_credito.html
│   ├── buscar_credito.html
│   ├── modificar_credito.html
│   └── crear_tablas.html
│
└── test/
    └── db_test.py             # 16 tests unitarios
```

---

## 🎯 Uso de la Aplicación Web

### Página Principal
Accede a http://localhost:5000 para ver el menú principal

### Insertar Crédito
1. Clic en "Insertar"
2. Completa el formulario
3. Clic en "Guardar Crédito"

### Buscar Crédito
1. Clic en "Buscar"
2. Ingresa el nombre
3. Ver resultados

### Modificar Crédito
1. Clic en "Modificar"
2. Busca por nombre
3. Actualiza campos
4. Guarda cambios

---

## 🔒 Seguridad

- ✅ Consultas parametrizadas
- ✅ Validaciones de formularios
- ✅ Credenciales en archivo separado
- ✅ Manejo de errores robusto

**Importante:** NO subas `secret_config.py` a repositorios públicos

---

## 🐛 Solución de Problemas

### Error: "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### Error: "could not translate host name"
Verifica que `PGHOST` tenga el FQDN completo

### Error: "relation creditos does not exist"
Crea las tablas: http://localhost:5000/crear_tablas

---

# SIMULADOR DE CRÉDITO EDUCATIVO (Versión Original)


Calcular el valor futuro del prestamo al finalizar el periodo de gracia
Calcular la cuota mensual durante el periodo de amortización,
dependiendo de la tasa de interes que le cobre la entidad del credito educativo.

# Proceso del Proyecto

## Variables de entrada
1. monto_credito: Valor del préstamo solicitado.
2. duracion_periodo_meses: Tiempo de estudio (periodo de gracia en meses).
3. tasa_interes_anual: Interés anual expresado en porcentaje.
4. plazo_amortizacion: Número de meses para pagar el crédito después de graduarse (entre 120 y 180 meses).


## Variables de salida
1. tasa_mensual: Tasa de interés mensual.
2. valor_a_pagar: Capital ajustado después del periodo de gracia.
3. cuota_mensual: Pago mensual del crédito.
4. total_a_pagar: Valor total del crédito al finalizar.
5. intereses_totales: Diferencia entre el total pagado y el monto original.

# Estructura del Proyecto
```
SIMULADOR_CREDITO_EDUCATIVO_PROYECT_SUSANA/
├── src/
│ ├── __init__.py
│ ├── model/
│ │ ├── __init__.py
│ │ └── monto.py # Lógica de negocio
│ └── view/
│ ├── __init__.py
│ ├── interfaz_credito.py # Interfaz en consola
│ └── interfaz_kivy.py # Interfaz gráfica con Kivy
├── tests/
│ ├── __init__.py
│ └── test_monto.py # Pruebas unitarias
├── README.md
└── requirements.txt
```
# Requisitos

Python 3.11+

Se recomienda entorno virtual (venv).

# Ejecutar la Interfaz Gráfica (Kivy)

### 1. Requisitos previos

Python 3.11+ instalado en tu máquina.

### 2. Clonar el repositorio y entrar al proyecto
```
git clone <URL_DEL_REPO>
cd ProyectoCreditoEducativo
```

### 3. Crear y activar entorno virtual (opcional pero recomendado)

Debes crear el entorno con python 3.11+

```
python -m venv .venv
```

### macOS / Linux:

```
source .venv/bin/activate
```

### Windows (PowerShell):


```
.venv\Scripts\Activate.ps1
```

### Windows (CMD):

```
.venv\Scripts\activate.bat
```
### 4. Instalar dependencias del proyecto
En la terminal ejecuta este comando:
```
pip install -r requirements.txt
```
### 5. Ejecutar la interfaz gráfica
Desde la raíz del proyecto ejecuta este comando:
```
python -m src.view.interfaz_kivy
```
O simplemente dale run(parte superior derecha) estando en el archivo interfaz_kivy
### 6. Uso
 Se abrirá una ventana de Kivy con los siguientes campos:

 -Monto del crédito

 -Periodo de gracia (meses)

 -Tasa de interés anual (%)

 -Plazo amortización (meses)

#### Ingresa los datos y haz clic en Calcular.
Verás en pantalla:

 -Tasa mensual

 -Valor futuro (capital ajustado al final del periodo de gracia)

 -Cuota mensual
 
 -Total a pagar
 
 -Intereses totales

### 7. Manejo de errores

Si ingresas datos inválidos, por ejemplo:

 -Monto = 0

 -Periodo de gracia = 0

 -Tasa de interés negativa

 -Plazo fuera del rango (menor a 120 o mayor a 180 meses)

 #### El sistema mostrará un mensaje de Error con la causa.

# Conectar base de datos

Conecta tu base de datos desde PotgresSQL y en el archivo
```
secret_config.py
```
Ingresa los siguientes datos:
 
 -PGHOST = 'PONGA EL HOST DE LA BD AQUI'
 
 -PGDATABASE = 'PONGA EL NOMBRE DE LA BASE DE DATOS AQUI'
 
 -PGUSER = 'PONGA EL USUARIO AQUI'
 
 -PGPASSWORD  = 'PONGA LA CONTRASEÑA AQUI'
 
 -PGPORT = 'PONGA EL PORT AQUI'


# Excel
https://docs.google.com/spreadsheets/d/1vUZCESrmqcjqwsqi9wNJCWLliLGc8mfN/edit?usp=sharing&ouid=112092804109599146567&rtpof=true&sd=true


# Autores

Susana Morales

# Autores Interfaz Gráfica y Correcciones

Juan Esteban Echavarria 

Mariana Henao
