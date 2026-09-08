class Node:


    def __init__(self, p=None, l=None, r=None, d=None):
        self.parent = p 
        self.left = l 
        self.right = r  
        self.data = d  

    def __str__(self):
   
        if self.data == None:
            return "None"
        else:
            return str(self.data.a1)  


class Data:


    def __init__(self, val1, val2):
        self.a1 = val1  
        self.a2 = val2  



def TreeSearch(x, k):
  
    if x == None or k == x.data.a1:
        return x 
    if k < x.data.a1:
        return TreeSearch(x.left, k)  
    else:
        return TreeSearch(x.right, k)  


def IterativeTreeSearch(x, k):
   
    while x != None and k != x.data.a1:
        if k < x.data.a1:
            x = x.left 
        else:
            x = x.right 
    return x 


def TreeMinimum(x):
   
    while x.left != None:
        x = x.left 
    return x 


def TreeMaximum(x):
   
    while x.right != None:
        x = x.right
    return x  


def TreeSuccessor(x):

    if x.right != None:
   
        return TreeMinimum(x.right)


    y = x.parent
    while y != None and x == y.right:
        x = y  
        y = y.parent  
    return y  


def InOrderTreeWalk(x):

    if x != None:
        InOrderTreeWalk(x.left)  
        print(x.data.a1) 
        InOrderTreeWalk(x.right)  


def TreeInsert(root, z):
   
    y = None  
    x = root  

    while x != None:
        y = x  
        if z.data.a1 < x.data.a1:
            x = x.left
        else:
            x = x.right

    z.parent = y

    if y == None:
        root = z  
    elif z.data.a1 < y.data.a1:
        y.left = z  
    else:
        y.right = z 

    return root  


def Transplant(root, u, v):
   
    if u.parent == None:
        root = v 
    elif u == u.parent.left:
        u.parent.left = v  
    else:
        u.parent.right = v  

    if v != None:
        v.parent = u.parent  

    return root


def TreeDelete(root, z):

    if z.left == None:
       
        root = Transplant(root, z, z.right)

    elif z.right == None:
        
        root = Transplant(root, z, z.left)

    else:
     
        y = TreeMinimum(z.right)

        if y.parent != z:
            root = Transplant(root, y, y.right)
            y.right = z.right
            y.right.parent = y

        root = Transplant(root, z, y)
        y.left = z.left
        y.left.parent = y

    return root
import random


def RandomData(min_val, max_val, el):
    N = []
    for i in range(el):
        a = random.randint(min_val, max_val)
        b = str(random.randint(min_val, max_val))
        D = Data(a, b)
        Nn = Node(d=D)
        N.append(Nn)
    return N


def PrintTree(root, level=0, prefix="Root: "):
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

    elNum = 7
    N = RandomData(0, elNum * 2, elNum)

    root = N[0]  
    print(f"Root: {N[0].data.a1}")

    for i in range(1, elNum):
        root = TreeInsert(root, N[i])
        print(f"Dodato: {N[i].data.a1}")

    PrintTree(root)

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

    print("\n" + "=" * 50)

    array = [50, 20, 75, 2, 27, 32, 80, 90, 26, 25]
    nodes = []

    for value in array:
        d = Data(value, str(value))
        n = Node(d=d)
        nodes.append(n)

    tree_root = nodes[0]
    print(f"Root: {tree_root.data.a1}")

    for i in range(1, len(nodes)):
        tree_root = TreeInsert(tree_root, nodes[i])
        print(f"added: {nodes[i].data.a1}")

    PrintTree(tree_root)

    InOrderTreeWalk(tree_root)

    print(f"\nPretraga 27: {TreeSearch(tree_root, 27) != None}")
    print(f"Pretraga 100: {TreeSearch(tree_root, 100) != None}")

    min_node = TreeMinimum(tree_root)
    max_node = TreeMaximum(tree_root)
    print(f"Minimum: {min_node.data.a1}")
    print(f"Maximum: {max_node.data.a1}")

    node_27 = TreeSearch(tree_root, 27)
    if node_27:
        succ = TreeSuccessor(node_27)
        print(f"Sledbenik od 27: {succ.data.a1 if succ else None}")

    tree_root = TreeDelete(tree_root, node_27)
    InOrderTreeWalk(tree_root)
