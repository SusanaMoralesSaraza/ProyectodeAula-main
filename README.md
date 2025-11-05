# 🎓 Sistema de Gestión de Créditos Educativos

Aplicación web completa para gestionar créditos educativos con interfaz moderna, desarrollada con Flask y PostgreSQL.

# SIMULADOR DE CRÉDITO EDUCATIVO (Versión Anterior)
Se requiere una aplicación que le permita a un estudiante saber cuál es la cuota mensual que deberá pagar a futuro si toma un crédito educativo (tipo Icetex) con periodo de gracia y en la modalidad de Largo Plazo (todos los pagos se hacen después de graduarse)


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

---

## 🚀 EJECUTAR LA APLICACIÓN LOCALMENTE CON BASE DE DATOS EN BLANCO

### Requisitos Previos
- Python 3.11 o superior
- Acceso a una base de datos PostgreSQL (puede ser Render, local, u otro servicio)

---

### Paso 1️⃣: Clonar y preparar el proyecto

```bash
# Clonar el repositorio
git clone https://github.com/SusanaMoralesSaraza/ProyectodeAula-main.git
cd ProyectodeAula-main-1

# Crear entorno virtual (RECOMENDADO)
python -m venv venv

# Activar entorno virtual
# En Windows PowerShell:
.\venv\Scripts\activate
# En Windows CMD:
venv\Scripts\activate.bat
# En Mac/Linux:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

---

### Paso 2️⃣: Configurar base de datos en blanco

Edita el archivo **`secret_config.py`** con las credenciales de tu base de datos PostgreSQL:

```python
# secret_config.py
PGHOST = 'Tu host de PostgreSQL'  
PGDATABASE = 'Nombre de tu base de datos'                      
PGUSER = 'tu_usuario'                                
PGPASSWORD = 'tu_contraseña'                        
PGPORT = '5432'                                      # Puerto (generalmente 5432)
```

**Importante:** 
- Si usas Render, copia el "External Database URL" desde tu Dashboard y extrae los datos
- El formato es: `postgresql://usuario:contraseña@host/base_de_datos`

---

### Paso 3️⃣: Ejecutar la aplicación web

```bash
python app.py
```

Verás un mensaje como:
```
 * Running on http://127.0.0.1:5000
```

---

### Paso 4️⃣: Crear las tablas en la base de datos EN BLANCO

**Opción A - Desde el navegador (RECOMENDADO):**

1. Abre tu navegador
2. Ve a: **http://127.0.0.1:5000**
3. En el menú principal, haz clic en **"Crear Tablas"**
4. Haz clic en el botón **"Crear Tablas Ahora"**
5. Verás un mensaje de éxito: ✅ "Tablas creadas exitosamente"

**Opción B - Desde la terminal:**

```bash
python -c "from src.controller.controlador_creditos import ControladorCreditos; ControladorCreditos.crear_tablas(); print('✅ Tablas creadas exitosamente')"
```

**Opción C - Desde la interfaz de consola:**

```bash
python interfaz_consola.py
# Selecciona opción: 6. Inicializar Tablas
```

---

### Paso 5️⃣: Usar la aplicación

Una vez creadas las tablas, accede a: **http://127.0.0.1:5000**

**Funcionalidades disponibles:**

1. **Listar Créditos** - Ver todos los créditos registrados (tabla vacía al inicio)
2. **Insertar Crédito** - Agregar un nuevo crédito con:
   - Nombre del beneficiario
   - Monto del crédito
   - Duración del periodo (meses)
   - Tasa de interés anual (%)
   - Plazo de amortización (meses)
3. **Buscar Crédito** - Buscar por nombre del beneficiario
4. **Modificar Crédito** - Actualizar datos de un crédito existente
5. **Eliminar Crédito** - Borrar un crédito (con confirmación)

---

### 🌐 Desplegar en la Web (Render)

#### Paso 1: Subir a GitHub
```bash
git add .
git commit -m "Aplicación web de créditos educativos"
git push origin main
```

#### Paso 2: Crear Web Service en Render
1. Ve a https://dashboard.render.com/
2. Clic en **"New +" → "Web Service"**
3. Conecta tu repositorio de GitHub
4. Configuración:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Clic en **"Create Web Service"**

#### Paso 3: Crear tablas en producción
Una vez desplegado, visita: `https://tu-app.onrender.com/crear_tablas`

---

## 📁 Estructura del Proyecto

```
ProyectodeAula-main-1/
├── app.py                          # Aplicación Flask principal
├── secret_config.py                # Configuración de base de datos
├── requirements.txt                # Dependencias Python
├── Procfile                        # Configuración para deployment
├── src/
│   ├── model/
│   │   └── credito.py             # Modelo de datos
│   └── controller/
│       └── controlador_creditos.py # Lógica CRUD
├── templates/                      # Plantillas HTML
│   ├── base.html                  # Template base
│   ├── index.html                 # Página principal
│   ├── listar_creditos.html       # Ver todos
│   ├── insertar_credito.html      # Crear nuevo
│   ├── buscar_credito.html        # Buscar
│   ├── modificar_credito.html     # Editar
│   └── crear_tablas.html          # Inicializar BD
└── test/
    └── db_test.py                 # 16 tests unitarios
```

---

## 🔒 Seguridad

- ✅ Consultas SQL parametrizadas (protección contra SQL injection)
- ✅ Validación de formularios
- ✅ Manejo de errores con mensajes flash
- ⚠️ **NO subas `secret_config.py` a GitHub** (contiene credenciales)

---

## 🐛 Solución de Problemas

### Error: "could not translate host name"
- Verifica que `PGHOST` en `secret_config.py` tenga el hostname completo
- Ejemplo correcto: `dpg-xxxx-a.virginia-postgres.render.com`
- Ejemplo incorrecto: `dpg-xxxx-a.render.com` (falta región)

### Error: "relation creditos does not exist"
- La base de datos está en blanco
- Sigue el **Paso 4** para crear las tablas

### Error: "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

---


# Excel
https://docs.google.com/spreadsheets/d/1vUZCESrmqcjqwsqi9wNJCWLliLGc8mfN/edit?usp=sharing&ouid=112092804109599146567&rtpof=true&sd=true


# 🎓URL Sitio web
https://creditoeducativo.onrender.com


# Autores

Susana Morales

# Autores Interfaz Gráfica Kivy y Correcciones

Juan Esteban Echavarria 

Mariana Henao
