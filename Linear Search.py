def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


if __name__ == "__main__":
    arr = [90, 10, 40, 70, 5]
    
    num = int(input("Enter an Integer: "))
    result = linear_search(arr, num)
    
    if result == -1:
        print(f"The Number ({num}) Was Not Found.")
    else:
        print(f"The Number ({arr[result]}) Was Found At Index: ({result})")
