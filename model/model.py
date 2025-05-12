import networkx as nx
from database.DAO import DAO

class Model:

    def __init__(self):
        self._graph = nx.Graph()
        self._airports = DAO.getAllAirports()
        self._idMapAirports = {}
        for a in self._airports:
            self._idMapAirports[a.ID] = a

    def buildGraph(self, NMin):
        nodes = DAO.getAllNodes(int(NMin), self._idMapAirports)
        self._graph.add_nodes_from(nodes)

    def numNodi(self):
        return len(self._graph.nodes)

    def getNodi(self):
        return self._graph.nodes