def bubble_sort(arr):
    n = len(arr)
    flag = True
    c = 0
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = False
            c += 1
        if flag:
            break
    print("# of rounds:", c)

def print_array(arr):
    for num in arr:
        print(num, end=" ")
    print()

if __name__ == "__main__":
    arr = [30, 20, 40, 5, 60, 2]
    bubble_sort(arr)
    print_array(arr)
