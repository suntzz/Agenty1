from collections import defaultdict

class RedDeCT:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = defaultdict(list)
        self.tiempo = 0

    def agregar_arista(self, u, v):
        self.grafo[u].append(v)
        self.grafo[v].append(u)

    def encontrar_eslabones_debiles(self):
        visitado = [False] * self.V
        discovery_time = [float("Inf")] * self.V
        low = [float("Inf")] * self.V
        parent = [-1] * self.V
        eslabones_debiles = []

        for i in range(self.V):
            if not visitado[i]:
                self.DFS(i, visitado, discovery_time, low, parent, eslabones_debiles)

        return eslabones_debiles

    def DFS(self, u, visitado, discovery_time, low, parent, eslabones_debiles):
        visitado[u] = True
        discovery_time[u] = low[u] = self.tiempo
        self.tiempo += 1

        for v in self.grafo[u]:
            if not visitado[v]:
                parent[v] = u
                self.DFS(v, visitado, discovery_time, low, parent, eslabones_debiles)
                low[u] = min(low[u], low[v])

                if low[v] > discovery_time[u]:
                    eslabones_debiles.append((u, v))
            elif v != parent[u]:
                low[u] = min(low[u], discovery_time[v])

grafo_CT = RedDeCT(7)
aristas = [(0, 1), (0, 2), (1, 2), (2, 3), (3, 4), (4, 5), (4, 6), (5, 6)]

for u, v in aristas:
    grafo_CT.agregar_arista(u, v)

eslabones_debiles = grafo_CT.encontrar_eslabones_debiles()
print("Eslabones débiles:", eslabones_debiles)
