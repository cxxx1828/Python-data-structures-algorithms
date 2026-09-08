import random
import time
import class_example

def random_list (min, max, num_of_elements):
    list = random.sample(range(min, max), num_of_elements)
    return list



def print_list(L):
    print("List: ", L)


l = [25, 5,30,17,40,15,20,37, 42,10, 32,39,7,13,18,22,23,4]
print_list(l)

tree = class_example.Tree()

for i in l:
    node=class_example.Node(data=class_example.Data(i,str(i)))
    tree.tree_insert(node)

tree.print_tree()

print("\nInorder:")
tree.in_order_tree_walk(tree.root)


print("\n Iterative search tree:")
start_time = time.perf_counter()

for i in range (len(l)):
    print(tree.iterative_tree_search(tree.root, l[i]).data.a1) 

end_time = time.perf_counter()
print('Execution time is', end_time-start_time)

print("\n Tree search:")
start_time = time.perf_counter()

for i in range (0,len(l),2):
    print(tree.tree_search(tree.root, l[i]).data.a1)

end_time = time.perf_counter()
print('Execution time is', end_time-start_time)

print("\n Tree minimum:")
start_time = time.perf_counter()

print(tree.tree_minimum(tree.root).data.a1)

end_time = time.perf_counter()
print('Execution time is', end_time-start_time)

print("\n Tree maximum:")
start_time = time.perf_counter()

print(tree.tree_maximum(tree.root).data.a1)


end_time = time.perf_counter()
print('Execution time is', end_time-start_time)

print("\n Tree succesor:")
start_time = time.perf_counter()

print(tree.tree_successor(tree.tree_search(tree.root, 15)).data.a1)

end_time = time.perf_counter()
print('Execution time is', end_time-start_time)

print("\n Tree delete:")
start_time = time.perf_counter()

print(tree.tree_delete(tree.tree_search(tree.root, 20)))

end_time = time.perf_counter()
print('Execution time is', end_time-start_time)



tree.print_tree()



