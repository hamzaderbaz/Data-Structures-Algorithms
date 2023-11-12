def heapify(arr, n, i):
    l = 2 * i + 1
    r = 2 * i + 2
    max_val = i

    if l < n and arr[l] > arr[max_val]:
        max_val = l
    if r < n and arr[r] > arr[max_val]:
        max_val = r

    if max_val != i:
        arr[i], arr[max_val] = arr[max_val], arr[i]
        heapify(arr, n, max_val)

def build_heap(arr, n):
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

def heap_sort(arr, n):
    build_heap(arr, n)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

def print_array(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()

if __name__ == "__main__":
    arr = [90, 10, 40, 70, 5]
    n = len(arr)

    heap_sort(arr, n)
    print_array(arr, n)
