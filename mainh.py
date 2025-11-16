# import scheduler
# import ast
#
#
# def read_tasks_from_file(filename="snippets.txt"):
#     """Čita zadatke iz fajla"""
#     with open(filename, 'r') as file:
#         content = file.read().strip()
#
#         # Ako fajl sadrži "input = [...]", uzmi samo deo posle znaka =
#         if content.startswith('input ='):
#             content = content.split('=', 1)[1].strip()
#
#         # Parsiranje Python liste iz fajla
#         tasks = ast.literal_eval(content)
#         return tasks
#
#
# # Čitanje zadataka iz fajla
# input_tasks = read_tasks_from_file()
#
#
# def print_task(task, label=""):
#     if task:
#         print(f"{label}{task}")
#     else:
#         print(f"{label}None")
#
#
# def print_task_list(tasks, label=""):
#     print(f"{label}")
#     for task in tasks:
#         print(f"  {task}")
#     print()
#
#
# if __name__ == "__main__":
#     print("=== TEST PRIORITETNOG RASPOREĐIVAČA ===\n")
#
#     # Test 1: Dodavanje zadataka
#     print("1. Dodavanje zadataka...")
#     for task in input_tasks:
#         scheduler.add_new_task(task)
#     print(f"Dodano {len(input_tasks)} zadataka\n")
#
#     # Test 2: Sortiranje svih zadataka (od najnižeg ka najvišem prioritetu)
#     print("2. Sortiranje zadataka po prioritetu:")
#     sorted_tasks = scheduler.get_all_tasks_sorted()
#     print_task_list(sorted_tasks, "Sortirani zadaci (najniži -> najviši prioritet):")
#
#     # Test 3: Dobavljanje zadatka najvećeg prioriteta
#     print("3. Dobavljanje zadatka najvećeg prioriteta:")
#     next_task = scheduler.get_next_task()
#     print_task(next_task, "Zadatak najvećeg prioriteta: ")
#     print()
#
#     # Test 4: Smanjivanje prioriteta zadatka (rec3: 1 -> 10)
#     print("4. Povećavanje prioriteta zadatka rec3 sa 1 na 10:")
#     scheduler.decrease_task_priority('rec3', 10)
#     print("Prioritet zadatka rec3 promenjen na 10")
#
#     # Dobavljanje novog zadatka najvećeg prioriteta
#     next_task = scheduler.get_next_task()
#     print_task(next_task, "Novi zadatak najvećeg prioriteta: ")
#     print()
#
#     # Test 5: Dodavanje novog zadatka
#     print("5. Dodavanje novog zadatka rec7:")
#     new_task = {'priority': 7, 'start_time': 12, 'duration': 56, 'type': 'audio', 'recorder': 'rec7'}
#     scheduler.add_new_task(new_task)
#     print(f"Dodat zadatak: {new_task}")
#
#     # Prikaz svih preostalih zadataka
#     remaining_tasks = scheduler.get_all_tasks_sorted()
#     print_task_list(remaining_tasks, "\nPreostali zadaci (sortirani):")
#
#     # Test 6: Dodatni testovi
#     print("6. Dodatni testovi - dobavljanje po prioritetu:")
#     while scheduler.get_scheduler_size() > 0:
#         task = scheduler.get_next_task()
#         print_task(task, f"Sledeći zadatak (prioritet {task['priority']}): ")
#
#     print("\nSvi zadaci obrađeni!")
#     print(f"Broj preostalih zadataka: {scheduler.get_scheduler_size()}")

from scheduler import *

if __name__ == "__main__":
    input_data = [{'priority': 5, 'start_time': 10, 'duration': 20, 'type': 'audio', 'recorder': 'rec1'},
                  {'priority': 3, 'start_time': 15, 'duration': 10, 'type': 'video', 'recorder': 'rec2'},
                  {'priority': 1, 'start_time': 2, 'duration': 60, 'type': 'audio', 'recorder': 'rec3'},
                  {'priority': 6, 'start_time': 13, 'duration': 33, 'type': 'audio', 'recorder': 'rec4'},
                  {'priority': 2, 'start_time': 8, 'duration': 48, 'type': 'video', 'recorder': 'rec5'},
                  {'priority': 4, 'start_time': 26, 'duration': 25, 'type': 'video', 'recorder': 'rec6'}]

    tasks = []
    for i in input_data:
        tasks.append(Task(i['priority'], i['start_time'], i['duration'], i['type'], i['recorder']))

    # Sortiraj za prikaz
    sorted_tasks = GetAllTasksSorted(tasks)
    for task in sorted_tasks:
        print(task)

    # Kreiraj max heap za GetNextTask
    BuildMaxHeap(tasks)

    print("Get task:")
    print(GetNextTask(tasks))
    print(GetNextTask(tasks))
    print(GetNextTask(tasks))
    print(GetNextTask(tasks))