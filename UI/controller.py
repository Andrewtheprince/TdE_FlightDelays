import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizzaAeroporti(self, e):
        numCompagnie = self._view._txtInNumero.value
        if numCompagnie == "":
            self._view.create_alert(f"Devi inserire un valore minimo di compagnie aeree!")
            return
        try:
            numCompagnie = int(numCompagnie)
        except ValueError:
            self._view.create_alert(f"Devi inserire un valore numerico!")
            return
        print(numCompagnie)

    def handleTestConnessione(self, e):
        pass
