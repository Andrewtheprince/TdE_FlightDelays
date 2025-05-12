import flet as ft


class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def handleAnalizza(self, e):
        numCompagnie = self._view._txtInCMin.value
        if numCompagnie == "":
            self._view.create_alert(f"Devi inserire un valore minimo di compagnie aeree!")
            return
        try:
            numCompagnie = int(numCompagnie)
        except ValueError:
            self._view.create_alert(f"Devi inserire un valore numerico!")
            return
        self._model.buildGraph(numCompagnie)
        self._view.txt_result.controls.append(ft.Text(f"Creato grafo con {self._model.numNodi()} nodi"))
        airports = self._model.getNodi()
        for a in airports:
            self._view._ddAeroportoP.options.append(ft.dropdown.Option(a))
        self._view.update_page()

    def handleCerca(self, e):
        pass

    def handleConnessi(self, e):
        pass
