def binary_search(arr, element):
    l = 0
    h = len(arr) - 1
    while l <= h:
        m = (l + h) // 2

        if arr[m] == element:
            return m
        if arr[m] > element:
            h = m - 1
        else:
            l = m + 1

    return -1

if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    num = int(input("Enter an Integer: "))
    
    result = binary_search(arr, num)
    
    if result == -1:
        print(f"The Number: ({num}) Was Not Found.")
    else:
        print(f"The Number: ({arr[result]}) Was Found At Index: ({result})")
