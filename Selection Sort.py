def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] > arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def print_array(arr):
    for i in arr:
        print(i, end=" ")
    print()


if __name__ == "__main__":
    arr = [-60, 0, 50, 30, 10, 20]
    selection_sort(arr)
    print("Array After Selection Sort:")
    print_array(arr)
