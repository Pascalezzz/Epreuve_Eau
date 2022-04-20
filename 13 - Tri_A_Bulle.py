def bubbleSort(arr):
    if type(arr) != list:
        print("error")
        exit()
    
    if all(type(d) == int for d in arr) == False:
        print("error")
        exit()
    
    n = len(arr)

    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)

arr = [6, 5, 4, 3, 2, 1]
bubbleSort(arr)

arr = [6, 5, 4, "a", 2, 1]
bubbleSort(arr)