from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from src.model.monto import (
    conversion_tasa_anual,
    ErrorMonto,
    ErrorPeriodoGracia,
    ErrorDemasiadasCuotas,
)

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

    def calcular(self, _instance):
        try:
            monto = float(self.monto_input.text.strip())
            duracion = int(self.duracion_input.text.strip())
            tasa_anual = float(self.tasa_input.text.strip())
            plazo = int(self.plazo_input.text.strip())

            # usa la función del modelo que ya hace TODO (valida + convierte + calcula)
            tasa_mensual, valor_a_pagar, cuota_mensual, total, intereses = conversion_tasa_anual(
                monto_credito=monto,
                duracion_periodo_meses=duracion,
                tasa_interes_anual=tasa_anual,
                plazo_amortizacion=plazo,
            )

            self.resultado.text = (
                f"Tasa mensual: {tasa_mensual*100:.4f}%\n"
                f"Valor futuro: ${valor_a_pagar:,.2f}\n"
                f"Cuota mensual: ${cuota_mensual:,.2f}\n"
                f"Total a pagar: ${total:,.2f}\n"
                f"Intereses totales: ${intereses:,.2f}"
            )


        except (ValueError, ErrorMonto, ErrorPeriodoGracia, ErrorDemasiadasCuotas) as e:
            self.resultado.text = f"Error: {e}"

class CreditoApp(App):
    def build(self):
        return InterfazCredito()
    
if __name__ == "__main__":
    # Ejecuta desde la raíz del proyecto:
    #   python -m src.view.interfaz_kivy
    CreditoApp().run()