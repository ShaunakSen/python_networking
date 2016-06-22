def selection_sort(A):
    for i in range(0, len(A) - 1):
        minIndex = i
        for j in range(i + 1, len(A)):
            if A[j] < A[minIndex]:
                minIndex = j
        if minIndex != i:
            A[i], A[minIndex] = A[minIndex], A[i]

list1 = [7, 5, 4, 2, 1, 3, 8]

selection_sort(list1)
print list1
