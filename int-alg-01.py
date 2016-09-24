def sumAll(arr):
    if arr[0] > arr[1]:
        arr[0], arr[1] = arr[1], arr[0]
    return sum(range(arr[0],arr[1]+1))
