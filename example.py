import random
import time
import class_example
'''
    Generate random list of num_of_elements unique elements.
    Element value is in range [min, max)
'''
def random_list (min, max, num_of_elements):
    list = random.sample(range(min, max), num_of_elements)
    return list


'''
    Print elements in list L
'''
def print_list(L):
    print("List: ", L)


#l = random_list(0, 20, 10)      # create list of 10 elements where min element value is 0, and max 19
l = [25, 5,30,17,40,15,20,37, 42,10, 32,39,7,13,18,22,23,4]
print_list(l)

#Kreiranje stabla
tree = class_example.Tree()

#Dodavanje svih elemenata u stablo
for i in l:
    node=class_example.Node(data=class_example.Data(i,str(i)))
    tree.tree_insert(node)

#Graficki prikaz
print("\nStablo:")
tree.print_tree()

#InOrderTreeWalk
print("\nInorder:")
tree.in_order_tree_walk(tree.root)


#Iterative search
print("\n Iterative search tree:")
start_time = time.perf_counter()

for i in range (len(l)):
    print(tree.iterative_tree_search(tree.root, l[i]).data.a1) #.data.a1 bez ovoga nece ispisati vrednosti

end_time = time.perf_counter()
print('Execution time is', end_time-start_time)

#Tree search
print("\n Tree search:")
start_time = time.perf_counter()

for i in range (0,len(l),2):
    print(tree.tree_search(tree.root, l[i]).data.a1)

end_time = time.perf_counter()
print('Execution time is', end_time-start_time)

#Tree minimum
print("\n Tree minimum:")
start_time = time.perf_counter()

print(tree.tree_minimum(tree.root).data.a1)

end_time = time.perf_counter()
print('Execution time is', end_time-start_time)

#Tree maximum
print("\n Tree maximum:")
start_time = time.perf_counter()

print(tree.tree_maximum(tree.root).data.a1)


end_time = time.perf_counter()
print('Execution time is', end_time-start_time)

#Tree successor
print("\n Tree succesor:")
start_time = time.perf_counter()

print(tree.tree_successor(tree.tree_search(tree.root, 15)).data.a1)

end_time = time.perf_counter()
print('Execution time is', end_time-start_time)

#Tree delete
print("\n Tree delete:")
start_time = time.perf_counter()

print(tree.tree_delete(tree.tree_search(tree.root, 20)))

end_time = time.perf_counter()
print('Execution time is', end_time-start_time)



tree.print_tree()



