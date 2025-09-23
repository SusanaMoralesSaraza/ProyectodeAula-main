# src/view/interfaz_credito.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from src.model.monto import calcular_valor_futuro, calcular_cuota_mensual

class InterfazCredito(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        # Entradas
        self.monto_input = TextInput(hint_text="Monto del crédito", input_filter="float")
        self.duracion_input = TextInput(hint_text="Periodo de gracia (meses)", input_filter="int")
        self.tasa_input = TextInput(hint_text="Tasa de interés anual (%)", input_filter="float")
        self.plazo_input = TextInput(hint_text="Plazo amortización (meses)", input_filter="int")

        # Botón
        self.boton = Button(text="Calcular", on_press=self.calcular)

        # Resultado
        self.resultado = Label(text="Resultados aparecerán aquí")

        # Agregar widgets
        self.add_widget(self.monto_input)
        self.add_widget(self.duracion_input)
        self.add_widget(self.tasa_input)
        self.add_widget(self.plazo_input)
        self.add_widget(self.boton)
        self.add_widget(self.resultado)

    def calcular(self, instance):
        try:
            monto = float(self.monto_input.text)
            duracion = int(self.duracion_input.text)
            tasa = float(self.tasa_input.text)
            plazo = int(self.plazo_input.text)

            futuro = calcular_valor_futuro(monto, tasa, duracion)
            cuota = calcular_cuota_mensual(futuro, tasa, plazo)

            self.resultado.text = f"Valor futuro: {futuro:.2f}\nCuota mensual: {cuota:.2f}"
        except Exception as e:
            self.resultado.text = f"Error: {e}"

class CreditoApp(App):
    def build(self):
        return InterfazCredito()
    
if __name__ == "__main__":
    CreditoApp().run()