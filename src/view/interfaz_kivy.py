import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView

from src.model.monto import (
    conversion_tasa_anual,
    ErrorMonto,
    ErrorPeriodoGracia,
    ErrorDemasiadasCuotas,
)

def popup_mensaje(titulo: str, mensaje: str, *, ancho: int = 520, alto: int = 420) -> None:
    """Popup con scroll y WRAP de texto (no reutiliza widgets)."""
    root = BoxLayout(orientation="vertical", padding=16, spacing=10)

    sv = ScrollView(size_hint=(1, 1), do_scroll_x=False, bar_width=8)

    lbl = Label(
        text=mensaje,
        markup=True,      
        halign="left",
        valign="top",
        size_hint_y=None,  
    )

    def _wrap_text(*_):
        lbl.text_size = (sv.width - 16, None)    
        lbl.height = lbl.texture_size[1]

    sv.bind(size=_wrap_text)
    lbl.bind(texture_size=lambda *_: setattr(lbl, "height", lbl.texture_size[1]))

    sv.add_widget(lbl)

    btn_cerrar = Button(text="Cerrar", size_hint=(1, None), height=46)
    root.add_widget(sv)
    root.add_widget(btn_cerrar)

    pop = Popup(
        title=titulo,
        content=root,
        size_hint=(None, None),
        size=(ancho, alto),
        auto_dismiss=False,
    )
    btn_cerrar.bind(on_release=pop.dismiss)

    _wrap_text()  
    pop.open()


class InterfazCredito(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=12, spacing=8, **kwargs)

        # Entradas
        self.monto_input = TextInput(
            hint_text="Monto del crédito (ej: 20000000)",
            input_filter="float",
            multiline=False,
        )
        self.duracion_input = TextInput(
            hint_text="Periodo de gracia (meses, ej: 48)",
            input_filter="int",
            multiline=False,
        )
        self.tasa_input = TextInput(
            hint_text="Tasa de interés anual (%) (ej: 12)",
            input_filter="float",
            multiline=False,
        )
        self.plazo_input = TextInput(
            hint_text="Plazo amortización (meses 120–180)",
            input_filter="int",
            multiline=False,
        )

        # Botones
        self.boton_calcular = Button(text="Calcular", size_hint_y=None, height=44)
        self.boton_calcular.bind(on_press=self.calcular)

        self.boton_limpiar = Button(text="Limpiar", size_hint_y=None, height=44)
        self.boton_limpiar.bind(on_press=self.limpiar)

        self.boton_resumen = Button(text="Ver resumen", size_hint_y=None, height=44)
        self.boton_resumen.bind(on_press=self.ver_resumen_popup)

        # Resultado resumido en pantalla
        self.resultado = Label(text="Resultados aparecerán aquí", halign="left", valign="top")

        # Agregar widgets al layout
        for w in (
            self.monto_input,
            self.duracion_input,
            self.tasa_input,
            self.plazo_input,
            self.boton_calcular,
            self.boton_limpiar,
            self.boton_resumen,
            self.resultado,
        ):
            self.add_widget(w)

        # Cache del último resumen con markup (para el popup)
        self._ultimo_resumen_markup = ""

    def limpiar(self, _instance):
        self.monto_input.text = ""
        self.duracion_input.text = ""
        self.tasa_input.text = ""
        self.plazo_input.text = ""
        self.resultado.text = "Resultados aparecerán aquí"
        self._ultimo_resumen_markup = ""

    def _armar_resumen(self, tasa_mensual: float, valor: float, cuota: float, total: float, intereses: float) -> str:
        """Resumen con markup para el popup."""
        return (
            f"[b]Tasa mensual:[/b] {tasa_mensual*100:.4f}%\n"
            f"[b]Valor futuro:[/b] ${valor:,.2f}\n"
            f"[b]Cuota mensual:[/b] ${cuota:,.2f}\n"
            f"[b]Total a pagar:[/b] ${total:,.2f}\n"
            f"[b]Intereses totales:[/b] ${intereses:,.2f}"
        )

    def ver_resumen_popup(self, _instance):
        if not self._ultimo_resumen_markup:
            popup_mensaje("Resumen", "No hay resultados todavía. Ingresa datos y pulsa [b]Calcular[/b].")
            return

        # Mensaje personalizado + resultados
        mensaje = (
            "[b]Resumen del Crédito Educativo[/b]\n\n"
            "• Durante el periodo de gracia, el capital se capitaliza mensualmente.\n"
            "• La cuota mensual depende de la tasa y del plazo de amortización.\n\n"
            "Resultados de tu simulación:\n\n"
            f"{self._ultimo_resumen_markup}"
        )
        popup_mensaje("Resumen de la Simulación", mensaje)

    def calcular(self, _instance):
        try:
            # Validar campos vacíos
            if not all([
                self.monto_input.text.strip(),
                self.duracion_input.text.strip(),
                self.tasa_input.text.strip(),
                self.plazo_input.text.strip()
            ]):
                raise ValueError("Todos los campos son obligatorios. Por favor ingresa los valores.")

            monto = float(self.monto_input.text.replace(",", "").strip())
            duracion = int(self.duracion_input.text.strip())
            tasa_anual = float(self.tasa_input.text.strip())
            plazo = int(self.plazo_input.text.strip())

            tasa_mensual, valor, cuota, total, intereses = conversion_tasa_anual(
                monto_credito=monto,
                duracion_periodo_meses=duracion,
                tasa_interes_anual=tasa_anual,
                plazo_amortizacion=plazo,
            )

            # Cache para popup y versión sin markup en el label
            self._ultimo_resumen_markup = self._armar_resumen(
                tasa_mensual, valor, cuota, total, intereses
            )
            self.resultado.text = self._ultimo_resumen_markup.replace("[b]", "").replace("[/b]", "")

            popup_mensaje(
                "Cálculo exitoso",
                "La simulación se realizó correctamente.\nPulsa “Ver resumen” para ver el detalle."
            )

        except (ValueError, ErrorMonto, ErrorPeriodoGracia, ErrorDemasiadasCuotas) as exc:
            popup_mensaje("Error en los datos", str(exc))
        except Exception as exc:
            popup_mensaje("Error inesperado", f"Ocurrió un problema: {exc}")



class CreditoApp(App):
    def build(self):
        self.title = "Crédito"
        return InterfazCredito()


if __name__ == "__main__":
    CreditoApp().run()