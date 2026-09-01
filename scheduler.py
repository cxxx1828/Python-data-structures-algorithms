# import heapq
#
#
# class Task():
#     def __init__(self, priority, start_time, duration, type_val, recorder):
#         self.priority = priority
#         self.start_time = start_time
#         self.duration = duration
#         self.type = type_val
#         self.recorder = recorder
#         self.id = None
#
#
# class Taskscheduler():
#     def __init__(self):
#         self.heap = []
#         self.tasks = []
#         self.counter = 0
#
#
# # Globalna instanca
# task_scheduler = Taskscheduler()
#
#
# def add_new_task(new_task):
#     """Dodaje novi zadatak"""
#     t = Task(new_task['priority'], new_task['start_time'],
#              new_task['duration'], new_task['type'], new_task['recorder'])
#     t.id = task_scheduler.counter
#     task_scheduler.counter += 1
#
#     heapq.heappush(task_scheduler.heap, (-t.priority, t.id, t))
#     task_scheduler.tasks.append(t)
#
#
# def get_next_task():
#     """Vraća zadatak najvećeg prioriteta"""
#     if not task_scheduler.heap:
#         return None
#
#     priority, task_id, task = heapq.heappop(task_scheduler.heap)
#
#     task_scheduler.tasks = [t for t in task_scheduler.tasks if t.id != task_id]
#
#     return {
#         'priority': task.priority,
#         'start_time': task.start_time,
#         'duration': task.duration,
#         'type': task.type,
#         'recorder': task.recorder
#     }
#
#
# def decrease_task_priority(task_recorder, new_priority):
#     """Smanjuje prioritet zadatka"""
#     for task in task_scheduler.tasks:
#         if task.recorder == task_recorder:
#             task.priority = new_priority
#             rebuild_heap()
#             break
#
#
# def rebuild_heap():
#     """Ponovo gradi heap"""
#     task_scheduler.heap = []
#     for task in task_scheduler.tasks:
#         heapq.heappush(task_scheduler.heap, (-task.priority, task.id, task))
#
#
# def get_all_tasks_sorted():
#     """Vraća sve zadatke sortirane po prioritetu"""
#     sorted_tasks = sorted(task_scheduler.tasks, key=lambda x: x.priority)
#
#     result = []
#     for task in sorted_tasks:
#         result.append({
#             'priority': task.priority,
#             'start_time': task.start_time,
#             'duration': task.duration,
#             'type': task.type,
#             'recorder': task.recorder
#         })
#     return result
#
#
# def get_scheduler_size():
#     """Vraća broj zadataka"""
#     return len(task_scheduler.tasks)

#
# import math
#
#
#      class Task:
#
#          def __init__(self, p=None, s=None, d=None, t=None, r=None):
#              self.priority = p
#              self.start_time = s
#              self.duration = d
#              self.type = t
#              self.recorder = r
#
#          def __str__(self):
#              return ("P:" + str(self.priority) + ", S:" + str(self.start_time) + ", D:" + str(self.duration) + ", T:" + str(
#                  self.type) + ", R:" + str(self.recorder))
#
#
#      def Parent(i):
#          return i // 2
#
#
#      def Left(i):
#          return 2 * i + 1
#
#
#      def Right(i):
#          return 2 * i + 2
#
#
#      def MaxHeapify(A, i, heap_size):
#          l = Left(i)
#          r = Right(i)
#          if l < heap_size and A[l].priority > A[i].priority:
#              largest = l
#          else:
#              largest = i
#
#          if r < heap_size and A[r].priority > A[largest].priority:
#              largest = r
#          if largest != i:
#              A[i], A[largest] = A[largest], A[i]
#              MaxHeapify(A, largest, heap_size)
#
#
#      def BuildMaxHeap(A):
#          heap_size = len(A)
#          for i in range(heap_size // 2, -1, -1):
#              MaxHeapify(A, i, heap_size)
#
#
#      def HeapSort(A, heap_size):
#          BuildMaxHeap(A)
#          for i in range(len(A) - 1, 0, -1):
#              A[0], A[i] = A[i], A[0]
#              heap_size -= 1
#              MaxHeapify(A, 0, heap_size)
#
#
#      def GetNextTask(A):
#          el = A[0]
#          A.pop(0)
#          return el
#
#
#      def GetAllTasksSorted(A):
#          B = A[:]
#          HeapSort(B, len(B))
#          return B


#
# class Task:
#     def __init__(self, priority=None, start_time=None, duration=None, type=None, recorder=None):
#         self.priority = priority
#         self.start_time = start_time
#         self.duration = duration
#         self.type = type
#         self.recorder = recorder
#
#     def __str__(self):
#         return f"{{priority: {self.priority}, start_time: {self.start_time}, duration: {self.duration}, type: {self.type}, recorder: {self.recorder}}}"
#
#
# def parent(i):
#     return (i - 1) // 2
#
#
# def left(i):
#     return 2 * i + 1
#
#
# def right(i):
#     return 2 * i + 2
#
#
# def max_heapify(A, i, heap_size):
#     l = left(i)
#     r = right(i)
#
#     if l < heap_size and A[l].priority > A[i].priority:
#         largest = l
#     else:
#         largest = i
#
#     if r < heap_size and A[r].priority > A[largest].priority:
#         largest = r
#
#     if largest != i:
#         A[i], A[largest] = A[largest], A[i]
#         max_heapify(A, largest, heap_size)
#
#
# def build_max_heap(A):
#     heap_size = len(A)
#     for i in range(heap_size // 2 - 1, -1, -1):
#         max_heapify(A, i, heap_size)
#
#
# def heap_sort(A):
#     build_max_heap(A)
#     heap_size = len(A)
#     for i in range(len(A) - 1, 0, -1):
#         A[0], A[i] = A[i], A[0]
#         heap_size -= 1
#         max_heapify(A, 0, heap_size)
#
#
# task_heap = []
#
#
# def get_next_task():
#     if len(task_heap) == 0:
#         return None
#
#     max_task = task_heap[0]
#     task_heap[0] = task_heap[len(task_heap) - 1]
#     task_heap.pop()
#
#     if len(task_heap) > 0:
#         max_heapify(task_heap, 0, len(task_heap))
#
#     return max_task
#
#
# def decrease_task_priority(recorder, new_priority):
#     task_index = -1
#     for i in range(len(task_heap)):
#         if task_heap[i].recorder == recorder:
#             task_index = i
#             break
#
#     if task_index == -1:
#         print(f"Zadatak sa recorder {recorder} nije pronađen")
#         return
#
#     old_priority = task_heap[task_index].priority
#     if new_priority >= old_priority:
#         print("Nova vrednost prioriteta mora biti manja od trenutne")
#         return
#
#     task_heap[task_index].priority = new_priority
#     max_heapify(task_heap, task_index, len(task_heap))
#
#
# def add_new_task(new_task):
#     task_heap.append(new_task)
#
#     i = len(task_heap) - 1
#     while i > 0 and task_heap[parent(i)].priority < task_heap[i].priority:
#         task_heap[i], task_heap[parent(i)] = task_heap[parent(i)], task_heap[i]
#         i = parent(i)
#
#
# def get_all_tasks_sorted():
#     if len(task_heap) == 0:
#         return []
#
#     sorted_tasks = [Task(t.priority, t.start_time, t.duration, t.type, t.recorder)
#                     for t in task_heap]
#
#     heap_sort(sorted_tasks)
#     return sorted_tasks
#
#
# def initialize_scheduler(task_list):
#     global task_heap
#     task_heap = []
#
#     for task_dict in task_list:
#         task = Task(
#             priority=task_dict['priority'],
#             start_time=task_dict['start_time'],
#             duration=task_dict['duration'],
#             type=task_dict['type'],
#             recorder=task_dict['recorder']
#         )
#         task_heap.append(task)
#
#     build_max_heap(task_heap)


import math


class Task:
    

    def __init__(self, p=None, s=None, d=None, t=None, r=None):
        self.priority = p  # Prioritet zadatka (veći broj = viši prioritet)
        self.start_time = s  # Vreme početka snimanja
        self.duration = d  # Trajanje snimanja u minutama
        self.type = t  # Tip snimanja ('audio', 'video', ili 'audio+video')
        self.recorder = r  # Identifikator snimača (npr. 'rec1', 'rec2')

    def __str__(self):
        """Formatira zadatak za ispis u čitljivom obliku"""
        return ("P:" + str(self.priority) + ", S:" + str(self.start_time) +
                ", D:" + str(self.duration) + ", T:" + str(self.type) +
                ", R:" + str(self.recorder))


# OSNOVNE HEAP FUNKCIJE - za navigaciju kroz binarno stablo u nizu

def Parent(i):
    
    return (i - 1) // 2


def Left(i):
   
    return 2 * i + 1


def Right(i):
    
    return 2 * i + 2



def MaxHeapify(A, i, heap_size):
    
    l = Left(i)  # Pozicija levog deteta
    r = Right(i)  # Pozicija desnog deteta

    if l < heap_size and A[l].priority > A[i].priority:
        largest = l  # Levo dete je najveće
    else:
        largest = i  # Trenutni čvor je najveći od sebe i levog deteta

    if r < heap_size and A[r].priority > A[largest].priority:
        largest = r  # Desno dete je najveće

    if largest != i:
        A[i], A[largest] = A[largest], A[i]  # Zameni elemente
        MaxHeapify(A, largest, heap_size)  # Rekurzivno pozovi za novo mesto



def BuildMaxHeap(A):
   
    heap_size = len(A)
    # Poslednji čvor koji ima decu je na poziciji len//2 - 1
    for i in range(heap_size // 2 - 1, -1, -1):
        MaxHeapify(A, i, heap_size)



def HeapSort(A, heap_size):
    
    BuildMaxHeap(A)  # Napravi max heap

    # Sortiranje: stavljaj najveće elemente na kraj
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]  # Zameni najveći sa poslednjim
        heap_size -= 1  # Smanji heap
        MaxHeapify(A, 0, heap_size)  # Obnovi heap svojstvo


# PRIORITETNI RASPOREĐIVAČ FUNKCIJE

def GetNextTask(A):
   
    if len(A) == 0:
        return None  # Prazan heap

    max_task = A[0]  # Sačuvaj najveći element (root)
    A[0] = A[len(A) - 1]  # Stavi poslednji element na vrh
    A.pop()  # Ukloni poslednji element

    if len(A) > 0:
        MaxHeapify(A, 0, len(A))  # Obnovi heap svojstvo od root-a

    return max_task  # Vrati najveći element


def GetAllTasksSorted(A):
   
    B = A[:]  # Napravi kopiju da ne uništi originalni niz
    HeapSort(B, len(B))  # Sortiraj kopiju
    return B  # Vrati sortiranu kopiju
