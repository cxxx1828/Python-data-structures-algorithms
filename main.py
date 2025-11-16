
import random
import time
import math
from collections import defaultdict


class Node:
    """
    Tree node: left child, right child and data
    """

    def __init__(self, parent=None, left=None, right=None, data=None):
        """
        Node constructor
        @param A node data object
        """
        self.parent = parent
        self.left = left
        self.right = right
        self.data = data


class Data:
    """
    Tree data: datacenter name and capacity
    """

    def __init__(self, name, capacity):
        self.name = name  # ime datacentra (string), "USA-1"
        self.capacity = capacity  # kapacitet (int), 250

    def __str__(self):
        return f"{self.name} ----- {self.capacity}"

    def __repr__(self):
        return f"Data(name='{self.name}', capacity={self.capacity})"


class Tree:
    """
    Tree: root
    Methods: insert, inorder_tree_walk, search, search_iterative,
            minimum, maximum, successor, delete, print
    """

    def __init__(self, root=None):
        self.root = root

    def tree_insert(self, z):
        """
        TREE-INSERT(T, z)
        1  y = NIL
        2  x = T.root
        3  while x ≠ NIL
        4      y = x
        5      if z.key < x.key
        6          x = x.left
        7      else x = x.right
        8  z.p = y
        9  if y == NIL
        10     T.root = z
        11 elseif z.key < y.key
        12     y.left = z
        13 else y.right = z
        """
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.data.capacity < x.data.capacity:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:# ako je bilo prazno
            self.root = z
        elif z.data.capacity < y.data.capacity:
            y.left = z
        else:
            y.right = z

    def tree_search(self, x, k):
        """
        ITERATIVE-TREE-SEARCH(x, k)
        1  while x ≠ NIL and k ≠ x.key
        2      if k < x.key
        3          x = x.left
        4      else x = x.right
        5  return x
        """
        while x is not None and k != x.data.capacity:
            if k < x.data.capacity:
                x = x.left
            else:
                x = x.right
        return x

    def TreeSearch(self, k):
        """
        vraca tuple (Node, vreme_u_nanosekundama)
        wrapper funkcija za merenje vremena pretrage
        """
        start = time.perf_counter_ns()
        result = self.tree_search(self.root, k)
        end = time.perf_counter_ns()
        return (result, end - start)

    def inOrderTreePrint(self, x): #x je cvor od kog pocinjem
        """
        INORDER-TREE-WALK(x)
        1  if x ≠ NIL
        2      INORDER-TREE-WALK(x.left)
        3      print x.key
        4      INORDER-TREE-WALK(x.right)
        """
        if x is not None:
            self.inOrderTreePrint(x.left)
            print(x.data.name, "-----", x.data.capacity)
            self.inOrderTreePrint(x.right)

    def print_tree(self):


        def display(root):
            """Returns list of strings, width, height, and horizontal coordinate of the root."""
            # No child.
            if root.right is None and root.left is None:
                line = '%s' % root.data
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            # Only left child.
            if root.right is None:
                lines, n, p, x = display(root.left)
                s = '%s' % root.data
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            # Only right child.
            if root.left is None:
                lines, n, p, x = display(root.right)
                s = '%s' % root.data
                u = len(s)
                first_line = s + x * '_' + (n - x) * ' '
                second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            # Two children.
            left, n, p, x = display(root.left)
            right, m, q, y = display(root.right)
            s = '%s' % root.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2

        lines, *_ = display(self.root)
        for line in lines:
            print(line)


def bucket_sort(A):
    """
    BUCKET-SORT(A)
    1  n = A.length
    2  let B[0..n-1] be a new array
    3  for i = 0 to n-1
    4      make B[i] an empty list
    5  for i = 1 to n
    6      insert A[i] into list B[⌊n * A[i]⌋]
    7  for i = 0 to n-1
    8      sort list B[i] with insertion sort
    9  concatenate the lists B[0], B[1], ..., B[n-1] together in order

    vremenska slozenost O(n) prosecno
    najgori slucaj O(n²)
    """
    if not A:
        return A

    n = len(A)

    # max vrednost capacity
    max_capacity = max(dc[1] for dc in A)

    # kreiramo buckets za svaki el
    buckets = []
    for i in range(n):
        buckets.append([])

    # rasporeda el u buckets
    for datacenter in A:
        capacity = datacenter[1]
        bucket_index = (n * capacity) // (max_capacity + 1)
        buckets[bucket_index].append(datacenter)

    # sortiranje
    for bucket in buckets:
        bucket.sort(key=lambda x: x[1])

    # spajanje sve nazad
    result = []
    for bucket in buckets:
        for element in bucket:
            result.append(element)

    return result


class Vertex:
    """cvor u grafu"""

    def __init__(self, p=None, d=None, name=None):
        self.p = p  # roditelj (parent)
        self.d = d  # distanca od source cvora
        self.name = name  # ime cvora

    def __str__(self):
        return str(self.name)


class Edge:
    """ivica u grafu"""

    def __init__(self, u=None, v=None, w=1):
        self.u = u  # pocetni cvor
        self.v = v  # krajnji cvor
        self.w = w  # tezina ivice

    def __str__(self):
        return f"{self.u.name} -> {self.v.name} (w:{self.w})"


class Graph:
    """graf"""

    def __init__(self, V=None, E=None):
        self.V = V if V is not None else []  # niz cvorova
        self.E = E if E is not None else []  # niz ivica

    def __str__(self):
        """
        4.a. preklopljeni operator __str__ koji ispisuje graf u obliku:
        src cvor -> dst cvor, w = tezina
        """
        if not self.E:
            return "Graf nema veze"

        result = []
        for edge in self.E:
            result.append(f"{edge.u.name} -> {edge.v.name}, w = {edge.w}")

        return "\n".join(result)



def get_weight(G, u, v):
    """
    vraca tezinu ivice izmedu cvorova u i v
    a ako ivica ne postoji, vraca beskonacnost

    """
    for i in G.E:
        if i.u == u and i.v == v:
            return i.w
    return math.inf


def initialize_single_source(G, s):
    """
    INITIALIZE-SINGLE-SOURCE(G, s)
    1  for each vertex v ∈ G.V
    2      v.d = ∞
    3      v.π = NIL
    4  s.d = 0

    inicijalizuje distance na beskonacnost i parent pokazivace na nista
    jer na početku NE ZNAMO kako stici do bilo kog cvora, pa pretpostavljamo da su svi nedostizni
    """
    for v in G.V:
        v.d = math.inf
        v.p = None
    s.d = 0  #distanca pocetnog cvora na 0 jer je vec tu odatle krecemo


def relax(G, u, v):
    """
    RELAX(u, v, w)
    1  if v.d > u.d + w(u, v)
    2      v.d = u.d + w(u, v)
    3      v.π = u

    relaksacija ivice pokusava da poboljsa najkracu putanju do v

    """
    if v.d > u.d + get_weight(G, u, v):
        v.d = u.d + get_weight(G, u, v)
        v.p = u


def print_path(G, s, v):
    """
    PRINT-PATH(G, s, v)
    1  if v == s
    2      print s
    3  elseif v.π == NIL
    4      print "no path from" s "to" v "exists"
    5  else PRINT-PATH(G, s, v.π)
    6      print v
    """
    if v is s:  #ako ti je trenutni cvor jednak source
        print(s)
    elif v.p is None: # ako v nema roditelj, tj p = 0 i nije izvor, znaci nema putanje
        print("no path from", s, "to", v, "exists")
    else:
        print_path(G, s, v.p)
        print(v)


def extract_min(Q):
    """
    EXTRACT-MIN(Q)
    pronalazi i uklanja cvor sa minimalnom distancom iz skupa Q
    """
    min_node = None
    min_dist = math.inf

    for node in Q:
        if node.d < min_dist:
            min_dist = node.d
            min_node = node

    if min_node is not None:
        Q.remove(min_node)

    return min_node


def get_neighbors(G, u):
    """
    vraca listu susednih cvorova za cvor u
    """
    neighbors = []
    for edge in G.E:#prolazi kroz sve ivice, i vidimo sve pocetne cvorove
        if edge.u == u:  #ako je u pocetni cvor, znaci ako pocinje od u
            neighbors.append(edge.v) #dodaj kao destinaciju v
    return neighbors


def dijkstra(G, s): #graf, pocetni cvor
    """
    DIJKSTRA(G, w, s)
    1  INITIALIZE-SINGLE-SOURCE(G, s)
    2  S = ∅
    3  Q = G.V
    4  while Q ≠ ∅
    5      u = EXTRACT-MIN(Q)
    6      S = S ∪ {u}
    7      for each vertex v ∈ G.Adj[u]
    8          RELAX(u, v, w)
    """

    initialize_single_source(G, s)

    # S je prazan skup
    # Q sadrzi sve cvorove
    Q = list(G.V)        # svi cvorovi u queue

    while Q:
        # izvuci cvor sa min distancom
        u = extract_min(Q)  # uzmi najblizi

        if u is None or u.d == math.inf:
            break

        # u je sad u skupu S
        # relax susedne ivice
        neighbors = get_neighbors(G, u)
        for v in neighbors:
            if v in Q:
                relax(G, u, v) # azuriraj distance
                # v.d ce se MENJATI od ∞ ka stvarnim vrednostima
                # v.p ce pokazivati odakle smo dosli


def findRoute(G, s, target=None):
    """
    koristi Dijkstra algoritam
    za nalazenje najkrace putanje sa najmanje gubitka paketa

    param: grag, pocetni i cilj cvor
    """

    dijkstra(G, s)

    if target is not None:
        print("\nPutanja od", s.name, "do", target.name, ":")
        if target.d == math.inf:
            print("Ne postoji putanja od", s.name, "do", target.name)
        else:
            print("Ukupan moguci gubitak pronadjene putanje:", target.d)
            print("Putanja: \n", end="")
            print_path(G, s, target)
            print()


def create_datacenter_list(num_entries):
    """
    Generates a list of datacenters with random capacity values,
    using a country name and a unique number for each entry.

    Args:
        num_entries (int): The number of datacenter entries to create.
                           Must be between 10 and 10,000.

    Returns:
        list: A list of lists, where each inner list contains a string
              (unique datacenter name) and an integer (random capacity).
    """

    countries = [
        "USA", "Germany", "Japan", "Brazil", "India", "Australia",
        "France", "China", "Canada", "Singapore"
    ]

    datacenters = []
    country_counts = defaultdict(int)

    for _ in range(num_entries):
        name_prefix = random.choice(countries)
        country_counts[name_prefix] += 1
        unique_name = f'{name_prefix}-{country_counts[name_prefix]}'
        capacity = random.randint(50, 500)
        datacenters.append([unique_name, capacity])

    return datacenters


# =============================================================================
# pozivanje funkcija
# =============================================================================

print('*' * 90)
print('prvi zadatak: Generisanje listi')
print('*' * 90)

my_datacenters10 = create_datacenter_list(10)
my_datacenters100 = create_datacenter_list(100)
my_datacenters1000 = create_datacenter_list(1000)
my_datacenters10000 = create_datacenter_list(10000)

print(f"Generated a list of {len(my_datacenters10)} datacenters.")
print(f"Generated a list of {len(my_datacenters100)} datacenters.")
print(f"Generated a list of {len(my_datacenters1000)} datacenters.")
print(f"Generated a list of {len(my_datacenters10000)} datacenters.")

print('=' * 80)
print('drugi zadatak: Binary Search Tree')
print('=' * 80)

# kreiranje stabla za 10 elemenata
tree_10 = Tree()
for datacenter in my_datacenters10:
    node = Node(data=Data(datacenter[0], datacenter[1]))
    tree_10.tree_insert(node)

print("\n" + "=" * 80)
print("2.a - InOrder ispis stabla (sortirano po kapacitetu):")
print("=" * 80)
tree_10.inOrderTreePrint(tree_10.root)

print("\nGraficki prikaz stabla:")
tree_10.print_tree()

print("\n" + "=" * 80)
print("2.b - TreeSearch metoda sa merenjem vremena")
print("=" * 80)
node, search_time = tree_10.TreeSearch(my_datacenters10[9][1])
if node:
    print(f"Pronadjen 10. element: {node.data.name} ----- {node.data.capacity}")
    print(f"Vreme pretrage: {search_time} ns")

print("\n" + "=" * 80)
print("2.c - Dictionary sa vremenima pretrage")
print("=" * 80)

# kreiranje svih stabala
tree_100 = Tree()
for datacenter in my_datacenters100:
    tree_100.tree_insert(Node(data=Data(datacenter[0], datacenter[1])))

tree_1000 = Tree()
for datacenter in my_datacenters1000:
    tree_1000.tree_insert(Node(data=Data(datacenter[0], datacenter[1])))

tree_10000 = Tree()
for datacenter in my_datacenters10000:
    tree_10000.tree_insert(Node(data=Data(datacenter[0], datacenter[1])))

# kreiranje dictionary-ja za sva stabla
dict_10 = {}
for datacenter in my_datacenters10:
    node, search_time = tree_10.TreeSearch(datacenter[1])
    if node:
        dict_10[datacenter[0]] = search_time

dict_100 = {}
for datacenter in my_datacenters100:
    node, search_time = tree_100.TreeSearch(datacenter[1])
    if node:
        dict_100[datacenter[0]] = search_time

dict_1000 = {}
for datacenter in my_datacenters1000:
    node, search_time = tree_1000.TreeSearch(datacenter[1])
    if node:
        dict_1000[datacenter[0]] = search_time

dict_10000 = {}
for datacenter in my_datacenters10000:
    node, search_time = tree_10000.TreeSearch(datacenter[1])
    if node:
        dict_10000[datacenter[0]] = search_time

print(f"\nDictionary za 10 elemenata:\n{dict_10}")
print(f"\nDictionary za 100 elemenata kreiran (prvih 5): {dict(list(dict_100.items())[:5])}")
print(f"Dictionary za 1000 elemenata kreiran (prvih 5): {dict(list(dict_1000.items())[:5])}")
print(f"Dictionary za 10000 elemenata kreiran (prvih 5): {dict(list(dict_10000.items())[:5])}")

print('\n' + '=' * 80)
print('ZADATAK 3: Sorting - Bucket Sort')
print('=' * 80)

# sortiranje svih listi
sorted_10 = bucket_sort(my_datacenters10)
sorted_100 = bucket_sort(my_datacenters100)
sorted_1000 = bucket_sort(my_datacenters1000)
sorted_10000 = bucket_sort(my_datacenters10000)

print("\nSortirana lista od 10 elemenata:")
for dc in sorted_10:
    print(f"{dc[0]} ----- {dc[1]}")

print("\n" + "=" * 80)
print("3.a - BST stabla od sortiranih listi (nebalansirana - naginje desno)")
print("=" * 80)

# kreiranje stabla od sortiranih listi
tree_10_sorted = Tree()
for datacenter in sorted_10:
    tree_10_sorted.tree_insert(Node(data=Data(datacenter[0], datacenter[1])))

tree_100_sorted = Tree()
for datacenter in sorted_100:
    tree_100_sorted.tree_insert(Node(data=Data(datacenter[0], datacenter[1])))

tree_1000_sorted = Tree()
for datacenter in sorted_1000:
    tree_1000_sorted.tree_insert(Node(data=Data(datacenter[0], datacenter[1])))

tree_10000_sorted = Tree()
for datacenter in sorted_10000:
    tree_10000_sorted.tree_insert(Node(data=Data(datacenter[0], datacenter[1])))

print("\nGraficki prikaz nebalansiranog stabla (10 elemenata):")
tree_10_sorted.print_tree()

print("\n" + "=" * 80)
print("3.b - Dictionary za sortirana stabla")
print("=" * 80)

# dictionary za sortirana stabla
dict_10_sorted = {}
for datacenter in sorted_10:
    node, search_time = tree_10_sorted.TreeSearch(datacenter[1])
    if node:
        dict_10_sorted[datacenter[0]] = search_time

dict_100_sorted = {}
for datacenter in sorted_100:
    node, search_time = tree_100_sorted.TreeSearch(datacenter[1])
    if node:
        dict_100_sorted[datacenter[0]] = search_time

dict_1000_sorted = {}
for datacenter in sorted_1000:
    node, search_time = tree_1000_sorted.TreeSearch(datacenter[1])
    if node:
        dict_1000_sorted[datacenter[0]] = search_time

dict_10000_sorted = {}
for datacenter in sorted_10000:
    node, search_time = tree_10000_sorted.TreeSearch(datacenter[1])
    if node:
        dict_10000_sorted[datacenter[0]] = search_time

print(f"\nDictionary za 10 sortiranih: {dict_10_sorted}")
print(f"Dictionary za 100 sortiranih (prvih 5): {dict(list(dict_100_sorted.items())[:5])}")
print(f"Dictionary za 1000 sortiranih (prvih 5): {dict(list(dict_1000_sorted.items())[:5])}")
print(f"Dictionary za 10000 sortiranih (prvih 5): {dict(list(dict_10000_sorted.items())[:5])}")

print("\n" + "=" * 80)
print("3.c - Podaci za grafove")
print("=" * 80)

# prosecna vremena pretrage
avg_time_10_unsorted = sum(dict_10.values()) / len(dict_10)
avg_time_100_unsorted = sum(dict_100.values()) / len(dict_100)
avg_time_1000_unsorted = sum(dict_1000.values()) / len(dict_1000)
avg_time_10000_unsorted = sum(dict_10000.values()) / len(dict_10000)

avg_time_10_sorted = sum(dict_10_sorted.values()) / len(dict_10_sorted)
avg_time_100_sorted = sum(dict_100_sorted.values()) / len(dict_100_sorted)
avg_time_1000_sorted = sum(dict_1000_sorted.values()) / len(dict_1000_sorted)
avg_time_10000_sorted = sum(dict_10000_sorted.values()) / len(dict_10000_sorted)

print("\nProsecna vremena pretrage (NESORTIRANA stabla):")
print(f"10 elemenata: {avg_time_10_unsorted:.2f} ns")
print(f"100 elemenata: {avg_time_100_unsorted:.2f} ns")
print(f"1000 elemenata: {avg_time_1000_unsorted:.2f} ns")
print(f"10000 elemenata: {avg_time_10000_unsorted:.2f} ns")

print("\nProsecna vremena pretrage (SORTIRANA stabla):")
print(f"10 elemenata: {avg_time_10_sorted:.2f} ns")
print(f"100 elemenata: {avg_time_100_sorted:.2f} ns")
print(f"1000 elemenata: {avg_time_1000_sorted:.2f} ns")
print(f"10000 elemenata: {avg_time_10000_sorted:.2f} ns")

print('\n' + '=' * 80)
print('ZADATAK 4: Graph - Mreza komunikacije izmedu datacentara')
print('=' * 80)

# kreiranje cvorova
brazil1 = Vertex(name="Brazil-1")
japan1 = Vertex(name="Japan-1")
australia1 = Vertex(name="Australia-1")
australia2 = Vertex(name="Australia-2")
brazil2 = Vertex(name="Brazil-2")
germany1 = Vertex(name="Germany-1")

V = [brazil1, japan1, australia1, australia2, brazil2, germany1]

# kreiranje ivica
E = [
    Edge(u=brazil1, v=japan1, w=260),
    Edge(u=japan1, v=australia1, w=200),
    Edge(u=japan1, v=germany1, w=1600),
    Edge(u=australia1, v=australia2, w=150),
    Edge(u=australia1, v=germany1, w=2000),
    Edge(u=australia2, v=brazil2, w=600),
    Edge(u=australia2, v=japan1, w=60),
    Edge(u=australia2, v=brazil1, w=1400),
    Edge(u=brazil2, v=germany1, w=360),
    Edge(u=brazil2, v=brazil1, w=400),
    Edge(u=germany1, v=brazil1, w=80)
]

G = Graph(V, E)

print("\n4.a\n")
print(G)

print("\n4.b i 4.c FindRoute funkcija:")
findRoute(G, japan1, brazil1)

# Na samom kraju, posle zadatka 4:
print("\n" + "=" * 80)
print("PODACI ZA GRAFOVE - copy/paste u matplotlib:")
print("=" * 80)
print(f"y_unsorted = [{avg_time_10_unsorted:.2f}, {avg_time_100_unsorted:.2f}, {avg_time_1000_unsorted:.2f}, {avg_time_10000_unsorted:.2f}]")
print(f"y_sorted = [{avg_time_10_sorted:.2f}, {avg_time_100_sorted:.2f}, {avg_time_1000_sorted:.2f}, {avg_time_10000_sorted:.2f}]")
