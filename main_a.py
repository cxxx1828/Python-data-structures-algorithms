import math
from math import inf


class Vertex:
    def __init__(self, name=None, x=0.0, y=0.0, g=inf, h=inf, f=inf, p=None):
        self.name = name
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.f = f
        self.p = p

    def __str__(self):
        return f"{self.name} (g:{self.g:.1f}, h:{self.h:.1f}, f:{self.f:.1f})"


class Edge:
    def __init__(self, u=None, v=None, w=1.0):
        self.u = u
        self.v = v
        self.w = w

    def __str__(self):
        return f"{self.u.name} -> {self.v.name}, w = {self.w}"


class Graph:
    def __init__(self, V=None, E=None):
        self.V = V if V is not None else []
        self.E = E if E is not None else []

    def __str__(self):
        if not self.E:
            return "Graf nema veze"
        return "\n".join(f"{e.u.name} -> {e.v.name}, w = {e.w}" for e in self.E)


def euclidean_distance(u, v):
    return math.sqrt((u.x - v.x) ** 2 + (u.y - v.y) ** 2)


def get_weight(G, u, v):
    for edge in G.E:
        if edge.u == u and edge.v == v:
            return edge.w
    return math.inf


def get_neighbors(G, u):
    return [edge.v for edge in G.E if edge.u == u]


def extract_min_f(Q):
    min_node = None
    min_f = math.inf
    for node in Q:
        if node.f < min_f:
            min_f = node.f
            min_node = node
    if min_node is not None:
        Q.remove(min_node)
    return min_node


def print_path(G, s, v):
    if v is s:
        print(s.name, end="")
    elif v.p is None:
        print("no path from", s.name, "to", v.name, "exists")
    else:
        print_path(G, s, v.p)
        print(" -> " + v.name, end="")


def initialize_a_star_source(G, s, target):
    for v in G.V:
        v.g = math.inf
        v.h = euclidean_distance(v, target)
        v.f = math.inf
        v.p = None
    s.g = 0.0
    s.f = s.g + s.h


def a_star_relax(G, u, v):
    w_uv = get_weight(G, u, v)
    if v.g > u.g + w_uv:
        v.g = u.g + w_uv
        v.f = v.g + v.h
        v.p = u


def a_star(G, s, target):
    initialize_a_star_source(G, s, target)
    open_set = [s]
    closed_set = set()

    while open_set:
        u = extract_min_f(open_set)

        if u is target:
            break

        closed_set.add(u)

        for v in get_neighbors(G, u):
            if v in closed_set:
                continue

            a_star_relax(G, u, v)

            if v not in open_set:
                open_set.append(v)


def findRouteAStar(G, s, target):
    a_star(G, s, target)

    print("\n" + "=" * 80)
    print(f"A* Pathfinding from {s.name} to {target.name}:")
    print("=" * 80)

    if target.g == math.inf:
        print("no path from", s.name, "to", target.name, "exists")
    else:
        print(f"Total path cost (g): {target.g:.2f}")
        print("Route: ", end="")
        print_path(G, s, target)
        print()


if __name__ == "__main__":
    brazil1 = Vertex(name="Brazil-1", x=10.0, y=20.0)
    japan1 = Vertex(name="Japan-1", x=40.0, y=80.0)
    australia1 = Vertex(name="Australia-1", x=80.0, y=90.0)
    australia2 = Vertex(name="Australia-2", x=90.0, y=50.0)
    brazil2 = Vertex(name="Brazil-2", x=30.0, y=10.0)
    germany1 = Vertex(name="Germany-1", x=15.0, y=60.0)

    V = [brazil1, japan1, australia1, australia2, brazil2, germany1]

    E = [
        Edge(u=brazil1, v=japan1, w=65.0),
        Edge(u=japan1, v=australia1, w=45.0),
        Edge(u=japan1, v=germany1, w=35.0),
        Edge(u=australia1, v=australia2, w=42.0),
        Edge(u=australia1, v=germany1, w=70.0),
        Edge(u=australia2, v=brazil2, w=72.0),
        Edge(u=australia2, v=japan1, w=58.0),
        Edge(u=australia2, v=brazil1, w=85.0),
        Edge(u=brazil2, v=germany1, w=52.0),
        Edge(u=brazil2, v=brazil1, w=22.0),
        Edge(u=germany1, v=brazil1, w=41.0)
    ]

    G = Graph(V, E)

    print("Graph Structure:\n", G)
    findRouteAStar(G, japan1, brazil1)
