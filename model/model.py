import networkx as nx
from networkx.classes import neighbors

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
        self.addAllArchiV1()

    def numNodi(self):
        return len(self._graph.nodes)

    def getNodi(self):
        return self._graph.nodes

    def numArchi(self):
        return len(self._graph.edges)

    def addAllArchiV1(self):
        allEdges = DAO.getAllEdgesV1(self._idMapAirports)
        for e in allEdges:
            if e.aeroportoP in self._graph and e.aeroportoA in self._graph:
                if self._graph.has_edge(e.aeroportoP, e.aeroportoA):
                    self._graph[e.aeroportoP][e.aeroportoA]["weight"] += e.peso
                else:
                    self._graph.add_edge(e.aeroportoP, e.aeroportoA, weight = e.peso)

    def getSortedNeighbours(self, node):
        vicini = self._graph.neighbors(node)
        viciniTuples = []
        for n in vicini:
            viciniTuples.append((n, self._graph[node][n]["weight"]))
        viciniTuples.sort(key=lambda x: x[1])
        return viciniTuples

    def getIdMap(self):
        return self._idMapAirports
