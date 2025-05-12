import flet as ft
from flet_core import MainAxisAlignment


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "FlightDelays"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("FlightDelays", color="blue", size=24)
        self._page.controls.append(self._title)
        self._txtInNumero = ft.TextField(label="Minimo Compagnie aeree")
        self._btnAnalizzaAeroporti = ft.ElevatedButton(text="Analizza Aeroporti", on_click=self._controller.handleAnalizzaAeroporti)
        row1 = ft.Row([self._txtInNumero, self._btnAnalizzaAeroporti], alignment=MainAxisAlignment.CENTER)
        self._ddAeroportoPartenza = ft.Dropdown(label="Aeroporto di partenza")
        self._txtSpaziatore = ft.Text(f"                                         ")
        row2 = ft.Row([self._ddAeroportoPartenza, self._txtSpaziatore], alignment=MainAxisAlignment.CENTER)
        self._ddAeroportoDestinazione = ft.Dropdown(label="Aeroporto di destinazione")
        self._btnTestConnessione = ft.ElevatedButton(text="Test Connessione", on_click=self._controller.handleTestConnessione)
        row3 = ft.Row([self._ddAeroportoDestinazione, self._btnTestConnessione],spacing=20 ,alignment=MainAxisAlignment.CENTER)
        self._page.add(row1, row2, row3)
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
