from enum import Enum
from math import inf

time = 0

class Vertex:
    def __init__(self, ime_korisnika=None, prezime_korisnika=None, broj_grupe=None, color=None, parent=None, distance=None, f=None):
        self.ime_korisnika = ime_korisnika
        self.prezime_korisnika = prezime_korisnika
        self.broj_grupe = broj_grupe
        self.color = color
        self.parent = parent
        self.distance = distance
        self.f = f

    def __str__(self):
        return f'ime: {self.ime_korisnika}, prezime: {self.prezime_korisnika}, grupa: {self.broj_grupe}'


class VertexColor(Enum):
    WHITE = 0
    GRAY = 127
    BLACK = 255


class Edge:
    def __init__(self, source=None, destination=None):
        self.source = source
        self.destination = destination


class Graph:
    def __init__(self, V=None, E=None):
        self.V = V if V is not None else []
        self.E = E if E is not None else []
        self.susedi = []

    def ima_prijatelje(self, s):
        counter = 0
        for e in self.E:
            if e.source is s:
                counter += 1
        return counter

    def __str__(self):
        result = 'Veze u grafu, ime 1 je source, ime 2 je destination:\n'
        for e in self.E:
            result += f'Ime 1: {e.source.ime_korisnika} -> Ime 2: {e.destination.ime_korisnika}\n'
        return result

    def funkcija(self, ime_korisnika, prezime_korisnika):
        list_korisnika = []
        grupe = []

        dfs(self)

        for v in self.V:
            if ime_korisnika == v.ime_korisnika and prezime_korisnika == v.prezime_korisnika:
                broj_prijatelja = self.ima_prijatelje(v)
                
                if broj_prijatelja == 1:
                    v.broj_grupe = 1
                    grupe.append(1)
                elif broj_prijatelja == 2:
                    v.broj_grupe = 2
                    grupe.append(2)
                elif broj_prijatelja == 3:
                    v.broj_grupe = 3
                    grupe.append(3)
                else:
                    v.broj_grupe = 0
                    grupe.append(0)

                list_korisnika.append(v)

        return {'grupe': grupe, 'list': list_korisnika}


def dfs(G):
    for u in G.V:
        u.color = VertexColor.WHITE
        u.parent = None

    global time
    time = 0

    for u in G.V:
        if u.color == VertexColor.WHITE:
            dfs_visit(G, u)


def get_adjacent_vertices(G, u):
    adjacent = []
    for e in G.E:
        if e.source is u:
            adjacent.append(e.destination)
    return adjacent


def print_path(G, s, v):
    if v is s:
        print(s)
    elif v.parent is None:
        print('No path from', s, 'to', v, 'exists')
    else:
        print_path(G, s, v.parent)
        print(v)


def dfs_visit(G, u):
    global time
    time = time + 1
    u.distance = time
    u.color = VertexColor.GRAY

    adjacent_vertices = get_adjacent_vertices(G, u)
    for v in adjacent_vertices:
        if v.color == VertexColor.WHITE:
            v.parent = u
            dfs_visit(G, v)

    time = time + 1
    u.f = time
    u.color = VertexColor.BLACK


# Create vertices
a = Vertex(ime_korisnika='Laza', prezime_korisnika='Lazarevic', broj_grupe=0)
b = Vertex(ime_korisnika='Jovan', prezime_korisnika='Jovanovic', broj_grupe=0)
c = Vertex(ime_korisnika='Isidora', prezime_korisnika='Sekulic', broj_grupe=0)
d = Vertex(ime_korisnika='Dragoljub', prezime_korisnika='Mihajlovic', broj_grupe=0)
e = Vertex(ime_korisnika='Borislav', prezime_korisnika='Pekic', broj_grupe=0)
f = Vertex(ime_korisnika='Ivo', prezime_korisnika='Andric', broj_grupe=0)
g = Vertex(ime_korisnika='Danica', prezime_korisnika='Maksimovic', broj_grupe=0)

# Create edges
E = []
e1 = Edge(source=a, destination=b)
e2 = Edge(source=a, destination=c)
e3 = Edge(source=b, destination=a)
e4 = Edge(source=c, destination=a)
e5 = Edge(source=d, destination=g)
e6 = Edge(source=g, destination=d)
e7 = Edge(source=e, destination=f)
e8 = Edge(source=f, destination=e)

E.append(e1)
E.append(e2)
E.append(e3)
E.append(e4)
E.append(e5)
E.append(e6)
E.append(e7)
E.append(e8)

# Create vertex list
V = [a, b, c, d, e, f, g]

# Create graph
G = Graph(V, E)

# Testing
print('Testiranje __str__')
print('\nIspis svih veza u grafu:')
print(G)

print('Ispis svih korisnika u grafu pre poziva funkcije')
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

G.funkcija('Laza', 'Lazarevic')
G.funkcija('Jovan', 'Jovanovic')
G.funkcija('Isidora', 'Sekulic')
G.funkcija('Dragoljub', 'Mihajlovic')
G.funkcija('Borislav', 'Pekic')
G.funkcija('Ivo', 'Andric')
G.funkcija('Danica', 'Maksimovic')

print('\nIspis svih korisnika u grafu nakon poziva funkcije')
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
