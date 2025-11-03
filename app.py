# Para las aplicaciones web creadas con Flask, debemos importar siempre el modulo 
from flask import Flask    

# Para poder servir plantillas HTML desde archivos, es necesario importar el modulo render_template
from flask import render_template, request

from model.credito import Credito 
from controlador_creditos import ControladorCreditos  

# Flask constructor: crea una variable que nos servirá para comunicarle a Flask
# la configuración que queremos para nuestra aplicación
app = Flask(__name__)     

# decorator: se usa para indicar el URL Path por el que se va a invocar nuestra función
@app.route('/')      
def hello():
    return render_template("credito.html")

@app.route('/insertar')      
def insertar():
    credito = Credito( nombre="Felipe", monto_credito = 25000000, duracion_periodo_meses = 72,
                                  tasa_interes_anual= 12, plazo_amortizacion = 140)
    credito.nombre = request.args["nombre"]
    credito.monto_credito = float( request.args["monto_credito"] )
    credito.duracion_periodo_meses = int( request.args["duracion_periodo_meses"] )
    credito.tasa_interes_anual = float( request.args["tasa_interes_anual"] )
    credito.plazo_amortizacion = int( request.args["plazo_amortizacion"])   

    ControladorCreditos.insertar( credito )
    return "Se guardo el credito en la base de datos"

# Esta linea permite que nuestra aplicación se ejecute individualmente
if __name__=='__main__':
   app.run( debug=True)

