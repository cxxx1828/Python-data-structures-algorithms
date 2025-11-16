class Node:
    """
    Čvor binarnog stabla pretrage (BST)
    Svaki čvor sadrži:
    - parent: pokazivač na roditeljski čvor
    - left: pokazivač na levo dete
    - right: pokazivač na desno dete
    - data: podatke koje čvor čuva (objekat klase Data)
    """

    def __init__(self, p=None, l=None, r=None, d=None):
        self.parent = p  # Pokazivač na roditeljski čvor (None za root)
        self.left = l  # Pokazivač na levo dete (None ako nema levo dete)
        self.right = r  # Pokazivač na desno dete (None ako nema desno dete)
        self.data = d  # Podatak koji čvor čuva (objekat Data klase)

    def __str__(self):
        """
        String reprezentacija čvora - prikazuje ključ (a1 vrednost)
        Koristi se za ispis čvora
        """
        if self.data == None:
            return "None"
        else:
            return str(self.data.a1)  # Vraća ključ po kome se pretražuje


class Data:
    """
    Klasa koja enkapsulira podatke u čvoru
    a1 - služi kao ključ za pretragu i poređenje
    a2 - dodatni podatak (može biti bilo koji tip)
    """

    def __init__(self, val1, val2):
        self.a1 = val1  # Glavni ključ (int) - po ovome se pretražuje stablo
        self.a2 = val2  # Dodatni podatak (string ili bilo koji tip)


# fun.py - BST ALGORITMI I FUNKCIJE

def TreeSearch(x, k):
    """
    REKURZIVNA PRETRAGA STABLA

    Traži čvor sa ključem k počevši od čvora x

    Algoritam:
    1. Ako je čvor prazan ili je ključ pronađen - vrati čvor
    2. Ako je traženi ključ manji od trenutnog - idi levo
    3. Inače idi desno
    4. Rekurzivno pozovi za odgovarajuće dete

    Vremenska složenost: O(h) gde je h visina stabla
    Prostorna složenost: O(h) zbog rekurzije
    """
    if x == None or k == x.data.a1:
        return x  # Pronašao ili stigao do kraja
    if k < x.data.a1:
        return TreeSearch(x.left, k)  # Traži u levom podstablu
    else:
        return TreeSearch(x.right, k)  # Traži u desnom podstablu


def IterativeTreeSearch(x, k):
    """
    ITERATIVNA PRETRAGA STABLA

    Ista logika kao rekurzivna, ali koristi petlju umesto rekurzije
    Efikasnija po pitanju memorije jer ne koristi stek poziva

    Vremenska složenost: O(h)
    Prostorna složenost: O(1) - konstantna memorija
    """
    while x != None and k != x.data.a1:
        if k < x.data.a1:
            x = x.left  # Idi levo ako je ključ manji
        else:
            x = x.right  # Idi desno ako je ključ veći
    return x  # Vraća pronađeni čvor ili None


def TreeMinimum(x):
    """
    PRONALAŽENJE MINIMUMA U STABLU

    Minimum je uvek najlevlji čvor u (pod)stablu
    Jednostavno idemo levo dokle god možemo

    Vremenska složenost: O(h)
    """
    while x.left != None:
        x = x.left  # Idi levo dokle god možeš
    return x  # Najlevlji čvor je minimum


def TreeMaximum(x):
    """
    PRONALAŽENJE MAKSIMUMA U STABLU

    Maksimum je uvek najdesnји čvor u (pod)stablu
    Jednostavno idemo desno dokle god možemo

    Vremenska složenost: O(h)
    """
    while x.right != None:
        x = x.right  # Idi desno dokle god možeš
    return x  # Najdesnији čvor je maksimum


def TreeSuccessor(x):
    """
    PRONALAŽENJE SLEDBENIKA ČVORA

    Sledbenik je čvor sa najmanjim ključem većim od x.ključa
    (sledeći u inorder redosledu)

    Algoritam:
    1. Ako x ima desno dete - sledbenik je minimum desnog podstabla
    2. Inače, idi naviše dok ne dođeš do čvora čiji si levo dete

    Vremenska složenost: O(h)
    """
    if x.right != None:
        # Slučaj 1: x ima desno dete
        # Sledbenik je minimum desnog podstabla
        return TreeMinimum(x.right)

    # Slučaj 2: x nema desno dete
    # Idi naviše dok ne dođeš do čvora čiji si levo dete
    y = x.parent
    while y != None and x == y.right:
        x = y  # Idi na roditelja
        y = y.parent  # Idi na deda
    return y  # Prvi predak čiji je x u levom podstablu


def InOrderTreeWalk(x):
    """
    INORDER OBILAZAK STABLA

    Algoritam:
    1. Obiđi levo podstablo
    2. Poseti trenutni čvor (ispiši)
    3. Obiđi desno podstablo

    Rezultat: čvorovi ispisani u sortiranom redosledu
    Vremenska složenost: O(n) - posećuje svaki čvor tačno jednom
    """
    if x != None:
        InOrderTreeWalk(x.left)  # Rekurzivno obiđi levo podstablo
        print(x.data.a1)  # Ispiši trenutni čvor
        InOrderTreeWalk(x.right)  # Rekurzivno obiđi desno podstablo


def TreeInsert(root, z):
    """
    UMETANJE NOVOG ČVORA U STABLO

    Algoritam:
    1. Kreni od root-a i traži poziciju za novi čvor
    2. Idi levo/desno u zavisnosti od ključa
    3. Kada dođeš do None pozicije, tu umetni novi čvor
    4. Povežи novi čvor sa roditeljem

    Vremenska složenost: O(h)
    """
    y = None  # y će biti roditelj novog čvora
    x = root  # Počni pretragu od root-a

    # Traži poziciju za umetanje
    while x != None:
        y = x  # Zapamti trenutni čvor kao potencijalnog roditelja
        if z.data.a1 < x.data.a1:
            x = x.left  # Idi levo ako je novi ključ manji
        else:
            x = x.right  # Idi desno ako je novi ključ veći ili jednak

    # Postavi roditelja novog čvora
    z.parent = y

    # Odluči da li je novi čvor levo ili desno dete
    if y == None:
        root = z  # Stablo je bilo prazno, novi čvor postaje root
    elif z.data.a1 < y.data.a1:
        y.left = z  # Novi čvor je levo dete
    else:
        y.right = z  # Novi čvor je desno dete

    return root  # Vrati (možda novi) root


def Transplant(root, u, v):
    """
    ZAMENA PODSTABLA

    Zamenjuje podstablo sa korenom u podstablom sa korenom v
    Ova funkcija se koristi kao pomoćna za brisanje čvorova

    Algoritam:
    1. Ako je u root, postavi v kao novi root
    2. Inače, povežи roditelja od u sa v
    3. Ako v nije None, povežи v sa roditeljem od u
    """
    if u.parent == None:
        # u je root stabla
        root = v  # v postaje novi root
    elif u == u.parent.left:
        # u je levo dete svog roditelja
        u.parent.left = v  # Povežи roditelja sa v
    else:
        # u je desno dete svog roditelja
        u.parent.right = v  # Povežи roditelja sa v

    if v != None:
        v.parent = u.parent  # Povežи v sa roditeljem od u

    return root


def TreeDelete(root, z):
    """
    BRISANJE ČVORA IZ STABLA

    Tri slučaja:
    1. z nema levo dete - zameni z sa desnim detetom
    2. z nema desno dete - zameni z sa levim detetom
    3. z ima oba deteta - zameni z sa njegovim sledbenikom

    Vremenska složenost: O(h)
    """
    if z.left == None:
        # Slučaj 1: z nema levo dete
        # Transplant desno podstablo na mesto z
        root = Transplant(root, z, z.right)

    elif z.right == None:
        # Slučaj 2: z nema desno dete
        # Transplant levo podstablo na mesto z
        root = Transplant(root, z, z.left)

    else:
        # Slučaj 3: z ima oba deteta
        # Pronađi sledbenika z (minimum desnog podstabla)
        y = TreeMinimum(z.right)

        if y.parent != z:
            # Sledbenik nije direktno dete od z
            # Prvo transplant sledbeniково desno dete na njegово mesto
            root = Transplant(root, y, y.right)
            # Povežи sledbenika sa desnim podstablom od z
            y.right = z.right
            y.right.parent = y

        # Transplant sledbenika na mesto z
        root = Transplant(root, z, y)
        # Povežи sledbenika sa levim podstablom od z
        y.left = z.left
        y.left.parent = y

    return root
# main.py - testiranje
import random


def RandomData(min_val, max_val, el):
    """Generiše random podatke"""
    N = []
    for i in range(el):
        a = random.randint(min_val, max_val)
        b = str(random.randint(min_val, max_val))
        D = Data(a, b)
        Nn = Node(d=D)
        N.append(Nn)
    return N


def PrintTree(root, level=0, prefix="Root: "):
    """Jednostavan grafički prikaz stabla"""
    if root != None:
        print(" " * (level * 4) + prefix + str(root.data.a1))
        if root.left != None or root.right != None:
            if root.left:
                PrintTree(root.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if root.right:
                PrintTree(root.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")


if __name__ == "__main__":
    print("=== BST TESTIRANJE SA FUNKCIJAMA ===")

    # Kreiranje test podataka
    elNum = 7
    N = RandomData(0, elNum * 2, elNum)

    print("Dodavanje čvorova:")
    root = N[0]  # Prvi čvor je root
    print(f"Root: {N[0].data.a1}")

    for i in range(1, elNum):
        root = TreeInsert(root, N[i])
        print(f"Dodato: {N[i].data.a1}")

    print("\nGrafički prikaz stabla:")
    PrintTree(root)

    print("\nInOrder obilazak:")
    InOrderTreeWalk(root)

    print(f"\nTreeSearch za 5: {TreeSearch(root, 5) != None}")
    print(f"IterativeTreeSearch za 5: {IterativeTreeSearch(root, 5) != None}")

    min_node = TreeMinimum(root)
    max_node = TreeMaximum(root)
    print(f"TreeMinimum: {min_node.data.a1 if min_node else None}")
    print(f"TreeMaximum: {max_node.data.a1 if max_node else None}")

    if len(N) > 3:
        successor = TreeSuccessor(N[3])
        print(f"N[3]={N[3].data.a1} TreeSuccessor: {successor.data.a1 if successor else None}")

        print(f"\nBrisanje čvora N[3] sa vrednošću {N[3].data.a1}")
        root = TreeDelete(root, N[3])
        print("InOrder posle brisanja:")
        InOrderTreeWalk(root)

    # Test sa zadatim nizom
    print("\n" + "=" * 50)
    print("TEST SA ZADATIM NIZOM [50, 20, 75, 2, 27, 32, 80, 90, 26, 25]")

    array = [50, 20, 75, 2, 27, 32, 80, 90, 26, 25]
    nodes = []

    for value in array:
        d = Data(value, str(value))
        n = Node(d=d)
        nodes.append(n)

    # Kreiranje stabla
    tree_root = nodes[0]
    print(f"Root: {tree_root.data.a1}")

    for i in range(1, len(nodes)):
        tree_root = TreeInsert(tree_root, nodes[i])
        print(f"Dodato: {nodes[i].data.a1}")

    print("\nGrafički prikaz:")
    PrintTree(tree_root)

    print("\nInOrder obilazak:")
    InOrderTreeWalk(tree_root)

    # Testiranje operacija
    print(f"\nPretraga 27: {TreeSearch(tree_root, 27) != None}")
    print(f"Pretraga 100: {TreeSearch(tree_root, 100) != None}")

    min_node = TreeMinimum(tree_root)
    max_node = TreeMaximum(tree_root)
    print(f"Minimum: {min_node.data.a1}")
    print(f"Maximum: {max_node.data.a1}")

    # Test sledbenika
    node_27 = TreeSearch(tree_root, 27)
    if node_27:
        succ = TreeSuccessor(node_27)
        print(f"Sledbenik od 27: {succ.data.a1 if succ else None}")

    # Test brisanja
    print(f"\nBrisanje čvora 27")
    tree_root = TreeDelete(tree_root, node_27)
    print("InOrder posle brisanja:")
    InOrderTreeWalk(tree_root)