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
        self.data = data  #vrednost, ujedno ce biti i kljuc

#dodata klasa
class Data:
    ''' Tree data: Any object which is used as a tree node data'''

    def __init__(self, val1,val2):
        '''Data constructor'''
        self.a1 = val1 # broj kao int, ovde ubaci 5
        self.a2 = val2 # broj kao karakter, ovde ubaci "pet"

    #automatski se poziva metoda kada pokusamo da printamo intigere
    def __str__(self):
        #prikaz kada se koristi print()
        return f"{self.a1}"

    def __repr__(self):
        #prikaz u interaktivnom modu / debbugeru
        return f"Data(a1={self.a1}, a2='{self.a2}')"

class Tree:

    # dodat konstruktor
    def __init__(self, root = None):
        self.root = root

    """
    Tree: root
    Methods: insert, inorder_tree_walk, search, search_iterative,
            minimum, maximum, successor, delete, print
    """

    def tree_insert(self,z):
        y = None
        x = self.root
        while x is not None: # da li sam mogla i !=None??
            y=x
            if z.data.a1 < x.data.a1:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None: #takodje da li moze is umesto ==??
            #Tree was empty, stablo je bilo prazno
            self.root = z
        elif z.data.a1 < y.data.a1:
            y.left = z
        else:
            y.right = z

    #ispis elemenata stabla inorder, ima jos preorder i postorder
    def in_order_tree_walk(self,x): #mora self, TO MI NIJE JASNO WDYM mora??
        if x is not None:
            self.in_order_tree_walk(x.left) # za sta zapravo sluzi to self?
            print(x.data.a1)
            self.in_order_tree_walk(x.right)

    #cvor od kog nadalje pretrazujemo stablo, k je kljuc koji trazimo
    def tree_search(self,x, k):
        if x is None or k == x.data.a1:
            return x
        if k < x.data.a1:
            return self.tree_search(x.left, k)
        else:
            return self.tree_search(x.right, k)

    #ista funkcija samo nije rekurzivna
    def iterative_tree_search(self,x, k):
        while x is not None and k != x.data.a1:
            if k < x.data.a1:
                x = x.left
            else:
                x = x.right
        return x

    def tree_minimum(self,x):
        while x.left is not None:
            x = x.left
        return x

    def tree_maximum(self,x):
        while x.right is not None:
            x = x.right
        return x

    def tree_successor(self,x):
        if x.right is not None:
            return self.tree_minimum(x.right)
        y= x.parent
        while y is not None and x == y.right:
            x=y
            y = y.parent
        return y

    def tree_delete(self,z):
        if z.left is None:
            self.transplant(z,z.right)
        elif z.right is None:
            self.transplant(z,z.left)
        else:
            y = self.tree_minimum(z.right)

            if y.parent != z:
                self.transplant(y,y.right)
                y.right = z.right
                y.righ.parent = y
            self.transplant(z,y)
            y.left = z.left
            y.left.parent = y



    def transplant(self,u,v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

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







