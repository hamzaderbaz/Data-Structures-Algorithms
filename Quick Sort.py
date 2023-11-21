def partition1(arr, l, h):
    p = arr[l]
    i = l
    j = h
    while i < j:
        while arr[i] <= p:
            i += 1
        while arr[j] > p:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[l], arr[j] = arr[j], arr[l]
    return j


def quick_sort1(arr, l, h):
    if l < h:
        piv = partition1(arr, l, h)
        quick_sort1(arr, l, piv)
        quick_sort1(arr, piv + 1, h)


def partition2(arr, iBegin, jEnd):
    i = iBegin
    j = jEnd
    pivLoc = i
    while True:
        while arr[pivLoc] <= arr[j] and pivLoc != j:
            j -= 1
        if pivLoc == j:
            break
        elif arr[pivLoc] > arr[j]:
            arr[j], arr[pivLoc] = arr[pivLoc], arr[j]
            pivLoc = j

        while arr[pivLoc] >= arr[i] and pivLoc != i:
            i += 1
        if pivLoc == i:
            break
        elif arr[pivLoc] < arr[i]:
            arr[i], arr[pivLoc] = arr[pivLoc], arr[i]
            pivLoc = i
    return pivLoc


def quick_sort2(arr, l, h):
    if l < h:
        piv = partition2(arr, l, h)
        quick_sort2(arr, l, piv - 1)
        quick_sort2(arr, piv + 1, h)


if __name__ == "__main__":
    arr = [2, -1, 4, 7, 0]
    n = len(arr)

    quick_sort2(arr, 0, n - 1)
    for i in arr:
        print(i, end=" ")
