print("JEDNOSTAVAN PRIMER - RAZLIKA U RANGE")
print("=" * 50)

heap = [10, 8, 6, 4, 2, 1]
print(f"Heap: {heap}")
print(f"len(heap) = {len(heap)}")
print(f"len(heap)//2 = {len(heap)//2}")  # = 3
print(f"len(heap)//2 - 1 = {len(heap)//2 - 1}")  # = 2

print("\n" + "="*30)
print("TESTIRAMO OBE VERZIJE:")
print("="*30)

print("\n ISPRAVNA VERZIJA:")
print("range(2, -1, -1)")
ispravna = list(range(2, -1, -1))
print(f"Rezultat: {ispravna}")

print("\n TVOJA VERZIJA:")
print("range(0, 2, -1)")
tvoja = list(range(0, 2, -1))
print(f"Rezultat: {tvoja}")

print("\n" + "="*30)
print("ŠTA SE DEŠAVA:")
print("="*30)

print("\ ISPRAVNA - range(2, -1, -1):")
print("• Počinje od 2")
print("• Ide unazad (-1)")
print("• Završava PRE -1 (dakle ide do 0)")
print("• Generiše: 2, 1, 0")
print("• To su TAČNO indeksi koji nam trebaju!")

print("\n TVOJA - range(0, 2, -1):")
print("• Počinje od 0")
print("• Treba da ide unazad (-1)")
print("• Treba da završi PRE 2")
print("• ALI 0 je MANJE od 2!")
print("• Kako da idemo UNAZAD od manjeg ka većem broju?")
print("• Python kaže: NEMOGUĆE! Vraća prazan niz []")

print("\n" + "="*30)
print("ANALOGIJA:")
print("="*30)
print("Zamišli da brojiš unazad:")
print("• 'Broji od 2 unazad do 0': 2, 1, 0 ")
print("• 'Broji od 0 unazad do 2': ??? NEMOGUĆE! ")
print("  (Kako da ideš unazad a da stigneš do VEĆEG broja?)")

print("\n" + "="*30)
print("PYTHON RANGE PRAVILO:")
print("="*30)
print("range(start, stop, step)")
print("• Ako je step pozitivan (+1): start < stop")
print("• Ako je step negativan (-1): start > stop")
print("")
print("Primeri:")
print("range(0, 5, 1)  → [0,1,2,3,4]  (0 < 5) ")
print("range(5, 0, -1) → [5,4,3,2,1]  (5 > 0) ")
print("range(0, 5, -1) → []           (0 < 5) ")

print("\n" + "="*30)
print("DEMONSTRACIJA SA HEAP:")
print("="*30)

def build_max_heap_correct(arr):
    print("ISPRAVNA VERZIJA:")
    for i in range(len(arr)//2 - 1, -1, -1):
        print(f"  Obrađujem index {i} (vrednost {arr[i]})")

def build_max_heap_your_way(arr):
    print(" TVOJA VERZIJA:")
    indices = list(range(0, len(arr)//2 - 1, -1))
    if not indices:
        print("  NIŠTA! Range je prazan!")
    else:
        for i in indices:
            print(f"  Obrađujem index {i}")

heap_test = [20, 15, 10, 5, 3, 8]
print(f"\nTest heap: {heap_test}")
print(f"Unutrašnji čvorovi (trebaju nam): 0, 1, 2")

build_max_heap_correct(heap_test)
print()
build_max_heap_your_way(heap_test)

print("\n" + "="*30)
print("ZAKLJUČAK:")
print("="*30)
print(" KORISTI: range(len(heap)//2 - 1, -1, -1)")
print("   • Počinje od poslednjeg unutrašnjeg čvora")
print("   • Ide unazad do root-a (index 0)")
print("   • Uvek radi!")
print("")
print(" NE KORISTI: range(0, len(heap)//2 - 1, -1)")
print("   • Pokušava ići unazad od manjeg ka većem")
print("   • Python vraća prazan niz")
print("   • Heap se neće napraviti!")
