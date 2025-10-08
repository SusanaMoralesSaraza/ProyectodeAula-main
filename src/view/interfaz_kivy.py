# --- Bootstrap robusto para ejecutable (PyInstaller) ---
import os, sys, types
from pathlib import Path

# 1) Desactiva el auto-import de deps de Kivy
os.environ["KIVY_NO_DEPS"] = "1"           # <--- CLAVE
os.environ["KIVY_NO_ARGS"] = "1"
os.environ["KIVY_GL_BACKEND"] = "sdl2"

if hasattr(sys, "_MEIPASS"):
    base = Path(sys._MEIPASS)

    # DLLs de SDL2 dentro del exe
    os.environ["PATH"] = str(base) + os.pathsep + os.environ.get("PATH", "")
    os.environ["PYSDL2_DLL_PATH"] = str(base)
    os.environ["KIVY_SDL2_PATH"]  = str(base)

    # (Opcional) si igual llegara a intentarlo, anulamos el import
    if "kivy_deps.sdl2" not in sys.modules:
        dummy = types.ModuleType("kivy_deps.sdl2")
        dummy.dep_bins = []
        sys.modules["kivy_deps.sdl2"] = dummy

    # Rutas de recursos packaged
    from kivy.resources import resource_add_path
    resource_add_path(str(base / "kivy_install"))
    resource_add_path(str(base / "kivy_install" / "data"))
    resource_add_path(str(base / "kivymd"))

# sys.path para `src/...`
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
# ----------------------------------------------------------------

# ----------------- IMPORTS KIVY/KIVYMD -----------------
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.toolbar import MDTopAppBar

from src.model.monto import (
    conversion_tasa_anual,
    ErrorMonto,
    ErrorPeriodoGracia,
    ErrorDemasiadasCuotas,
)

# ----------------- UTILIDADES -----------------
def dlg(titulo: str, mensaje: str) -> MDDialog:
    return MDDialog(
        title=titulo,
        text=mensaje,
        buttons=[MDFlatButton(text="Cerrar", on_release=lambda d: d.dismiss())],
    )

def _to_float(s: str) -> float:
    # Convierte "12 345,67" o "12345.67" a float
    s = s.replace(" ", "").replace(",", ".").strip()
    return float(s)

# ----------------- VISTA -----------------
class Vista(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.add_widget(MDTopAppBar(title="Crédito Educativo", elevation=2))

        header = MDBoxLayout(
            orientation="vertical", size_hint_y=None, padding=(dp(16), dp(14), dp(16), dp(6))
        )
        header.bind(minimum_height=header.setter("height"))
        header.add_widget(
            MDLabel(
                text="Simulador de Crédito Educativo",
                halign="center",
                font_style="H5",
                size_hint_y=None,
                height=dp(34),
            )
        )
        self.add_widget(header)

        scroll = ScrollView(size_hint=(1, 1))
        root = MDBoxLayout(
            orientation="vertical",
            size_hint=(1, None),
            padding=(dp(16), dp(16), dp(16), dp(24)),
            spacing=dp(16),
        )
        root.bind(minimum_height=root.setter("height"))
        scroll.add_widget(root)
        self.add_widget(scroll)

        self.center_box = MDBoxLayout(orientation="vertical", size_hint=(None, None), spacing=dp(16))
        self.center_box.bind(minimum_height=self.center_box.setter("height"))
        root.add_widget(self.center_box)

        def _sync_w(*_):
            self.center_box.width = min(Window.width - dp(32), dp(640))

        _sync_w()
        Window.bind(size=lambda *_: _sync_w())

        # -------- Formulario --------
        self.card_form = MDCard(
            orientation="vertical", padding=dp(16), radius=[dp(16)] * 4, elevation=2, size_hint=(1, None)
        )
        form = MDBoxLayout(orientation="vertical", spacing=dp(12), size_hint_y=None)
        form.bind(minimum_height=form.setter("height"))

        def _sync_form_height(*_):
            self.card_form.height = form.height + dp(32)

        form.bind(height=lambda *_: _sync_form_height())

        self.monto = MDTextField(
            hint_text="Monto del crédito (COP)",
            helper_text="Ej: 20000000",
            helper_text_mode="on_focus",
            size_hint_y=None,
            height=dp(56),
            input_filter="int",
        )
        self.gracia = MDTextField(
            hint_text="Periodo de gracia (meses)",
            helper_text="Ej: 48",
            helper_text_mode="on_focus",
            size_hint_y=None,
            height=dp(56),
            input_filter="int",
        )
        self.tasa = MDTextField(
            hint_text="Tasa de interés anual (%)",
            helper_text="Ej: 12",
            helper_text_mode="on_focus",
            size_hint_y=None,
            height=dp(56),
        )
        self.plazo = MDTextField(
            hint_text="Plazo amortización (meses 120–180)",
            helper_text="Ej: 120…180",
            helper_text_mode="on_focus",
            size_hint_y=None,
            height=dp(56),
            input_filter="int",
        )
        for w in (self.monto, self.gracia, self.tasa, self.plazo):
            form.add_widget(w)

        fila_btn = MDBoxLayout(orientation="horizontal", size_hint_y=None, height=dp(48))
        fila_btn.add_widget(MDBoxLayout())
        btns = MDBoxLayout(orientation="horizontal", size_hint=(None, None), height=dp(44), width=dp(220), spacing=dp(10))
        btns.add_widget(MDRaisedButton(text="Calcular", on_release=self.calcular))
        btns.add_widget(MDFlatButton(text="Limpiar", on_release=self.limpiar))
        fila_btn.add_widget(btns)
        form.add_widget(fila_btn)

        self.card_form.add_widget(form)
        self.center_box.add_widget(self.card_form)

        # -------- Resultado --------
        self.card_res = MDCard(
            orientation="vertical", padding=dp(16), radius=[dp(16)] * 4, elevation=1, size_hint=(1, None)
        )
        res = MDBoxLayout(orientation="vertical", spacing=dp(8), size_hint_y=None)
        res.bind(minimum_height=res.setter("height"))

        def _sync_res_height(*_):
            self.card_res.height = res.height + dp(32)

        res.bind(height=lambda *_: _sync_res_height())

        res.add_widget(MDLabel(text="Resultado", halign="left", font_style="H6", size_hint_y=None, height=dp(26)))
        self.resultado = MDLabel(text="", halign="left", size_hint_y=None, height=dp(24))
        res.add_widget(self.resultado)

        self.card_res.add_widget(res)
        self.center_box.add_widget(self.card_res)

        self._ultimo = ""
        self._dlg_exito = None
        self.card_res.bind(width=lambda *_: self._ajustar_resultado())

    # -------- Lógica de vista --------
    def _ajustar_resultado(self):
        self.resultado.text_size = (self.card_res.width - dp(32), None)
        self.resultado.texture_update()
        self.resultado.height = max(dp(24), self.resultado.texture_size[1])

    def _cerrar_exito(self, *_):
        if self._dlg_exito:
            self._dlg_exito.dismiss()
            self._dlg_exito = None

    def limpiar(self, *_):
        self.monto.text = self.gracia.text = self.tasa.text = self.plazo.text = ""
        self.resultado.text = ""
        self._ultimo = ""
        self._cerrar_exito()

    def _mostrar_exito(self, texto="Cálculo exitoso"):
        self._cerrar_exito()
        self._dlg_exito = MDDialog(
            title="Éxito", text=texto, buttons=[MDFlatButton(text="Cerrar", on_release=self._cerrar_exito)]
        )
        self._dlg_exito.open()

    def calcular(self, *_):
        try:
            if not all([self.monto.text.strip(), self.gracia.text.strip(), self.tasa.text.strip(), self.plazo.text.strip()]):
                raise ValueError("Todos los campos son obligatorios.")

            monto = _to_float(self.monto.text)
            gracia = int(self.gracia.text.strip())
            tasa = _to_float(self.tasa.text)
            plazo = int(self.plazo.text.strip())

            tm, valor, cuota, total, intereses = conversion_tasa_anual(
                monto_credito=monto,
                duracion_periodo_meses=gracia,
                tasa_interes_anual=tasa,
                plazo_amortizacion=plazo,
            )

            self._ultimo = (
                f"Tasa mensual: {tm*100:.4f}%\n"
                f"Valor futuro: ${valor:,.2f}\n"
                f"Cuota mensual: ${cuota:,.2f}\n"
                f"Total a pagar: ${total:,.2f}\n"
                f"Intereses totales: ${intereses:,.2f}"
            )
            self.resultado.text = self._ultimo
            self._ajustar_resultado()
            self._mostrar_exito("Cálculo exitoso")

        except (ValueError, ErrorMonto, ErrorPeriodoGracia, ErrorDemasiadasCuotas) as e:
            self._cerrar_exito()
            dlg("Error en los datos", str(e)).open()
        except Exception as e:
            self._cerrar_exito()
            dlg("Error inesperado", f"Ocurrió un problema: {e}").open()

# ----------------- APP -----------------
class CreditoApp(MDApp):
    def build(self):
        self.title = "Crédito Educativo"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Indigo"
        root = MDBoxLayout(orientation="vertical")
        root.add_widget(Vista())
        return root

if __name__ == "__main__":
    CreditoApp().run()
