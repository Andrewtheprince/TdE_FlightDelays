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
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Creato grafo con {self._model.numNodi()} nodi e {self._model.numArchi()} archi!"))
        airports = self._model.getNodi()
        for a in airports:
            self._view._ddAeroportoP.options.append(ft.dropdown.Option(key = a.AIRPORT, data = a))
            self._view._ddAeroportoD.options.append(ft.dropdown.Option(key = a.AIRPORT, data = a))
        self._view.update_page()

    def handleConnessi(self, e):
        node = self._view._ddAeroportoP.value
        if node is None or node == "":
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f"Attenzione selezionare un aeroporto di partenza"))
            return
        vicini = self._model.getSortedNeighbours(node)
        self._view.txt_result.controls.clear()
        for v in vicini:
            self._view.txt_result.controls.append(ft.Text(f"{v[0]} - peso: {v[1]}"))
        self._view.update_page()


    def handleCerca(self, e):
        pass


