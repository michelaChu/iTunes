import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._idMap = {}

    def buildGraph(self, d):
        self._graph.clear()
        self._graph.add_nodes_from(DAO.getAlbums(toMillisec(d)))
        self._idMap = {a.AlbumId: a for a in list(self._graph.nodes)}
        edges = DAO.getEdges(self._idMap)
        self._graph.add_edges_from(edges)

    def getConnessaDetails(self, v0):
        conn = nx.node_connected_component(self._graph, v0)
        durataTot = 0
        for c in conn:
            durataTot += c.totD
        return len(conn), toMinutes(durataTot)

    def getNodes(self):
        return list(self._graph.nodes)

    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)

def toMillisec(d):
    return d*60*1000

def toMinutes(d):
    return d/1000/60


