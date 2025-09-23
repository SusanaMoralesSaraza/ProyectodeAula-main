# SIMULADOR DE CRÉDITO EDUCATIVO
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
└── README.md
```
# Requisitos

Python 3.10+

Se recomienda entorno virtual (venv).

Dependencias: Kivy

# Como hacer funcionar el programa
* Tener instalado python anteriormente en la maquina en donde se quiera ejecutar el programa.
* Proceder a abrir la consola de la maquina y escribir el siguiente comando donde tambiens se colocara la dirección del proyecto en el cual se guardó.
* Ejemplo: "Carpeta donde se clonó el proyecto\ProyectodeAula-main>py src\view\console.py"

# Como ejecutar las pruebas unitarias

*desde el cmd nuevamente se ejecuta el siguiente comando: "Carpeta donde se clonó el proyecto\ProyectodeAula-main>py test\test.py"

# Como ejecutar la consola
Desde el cmd nuevamente tenemos el siguiente prompt: "Carpeta donde se clonó el proyecto\ProyectodeAula-main>py src\view\console

# Ejecutar la Interfaz Gráfica (Kivy)

### 1. Requisitos previos

Python 3.10+ instalado en tu máquina.

Instalar dependencias (en un entorno virtual recomendado):

pip install kivy

### 2. Clonar el repositorio y entrar al proyecto
```
git clone <URL_DEL_REPO>
cd ProyectoCreditoEducativo
```

### 3. Crear y activar entorno virtual (opcional pero recomendado)

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
pip install kivy
```
### 5. Ejecutar la interfaz gráfica
Desde la raíz del proyecto ejecuta este comando:
```
python -m src.view.interfaz_credito
```
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

# Excel
https://docs.google.com/spreadsheets/d/1vUZCESrmqcjqwsqi9wNJCWLliLGc8mfN/edit?usp=sharing&ouid=112092804109599146567&rtpof=true&sd=true


# Autores

Susana Morales

# Autores Interfaz Gráfica y Correcciones

Juan Esteban Echavarria 

Mariana Henao






