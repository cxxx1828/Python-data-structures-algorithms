

def counting_sort(A, B, k):
    # Kreiraj niz C sa k+1 elemenata
    C = [0] * (k + 1)

    # Brojanje elemenata - koristi drugi element tuple-a
    for j in range(len(A)):
        C[A[j][1]] = C[A[j][1]] + 1  # A[j][1] je broj iz tuple-a

    # Kumulativni zbir
    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1]

    # Sortiranje unazad
    for j in range(len(A) - 1, -1, -1):
        broj = A[j][1]  # Izvuci broj iz tuple-a
        B[C[broj] - 1] = A[j]  # Stavi ceo tuple
        C[broj] = C[broj] - 1

    return B

def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        #ubacim A[j] u sortirani niz A[1 .. j-1]
        j = i-1

        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j = j-1

        A[j+1] = key

def bucket_sort(A):
    num_buckets = 10  # Fiksno 10 bucket-a za index 0-99
    buckets = []

    for i in range(num_buckets):
        buckets.append([])

    for dictionary in A:
        index_vrednost = dictionary['index']
        koji_bucket = index_vrednost // 10  # 0-9→0, 10-19→1, itd.
        buckets[koji_bucket].append(dictionary)

    for bucket in buckets:
        bucket.sort(key=lambda x: x['index'])

    result = []
    for bucket in buckets:
        for element in bucket:
            result.append(element)

    return result

















