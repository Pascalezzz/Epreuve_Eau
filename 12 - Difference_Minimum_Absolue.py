def findMinDiff(arr):
    if type(arr) != list:
        print("error")
        exit()
    
    diff = 10**20
    n = len(arr)

    for i in range(n-1):
        for j in range(i+1,n):
            if abs(arr[i]-arr[j]) < diff:
                diff = abs(arr[i] - arr[j])
 
    print(diff)
 
nombres = [5, 1, 19, 21]
findMinDiff(nombres)

nombres=[20, 5, 1, 19, 21]
findMinDiff(nombres)

nombres=[ -8, -6, 4]
findMinDiff(nombres)

nombres="test"
findMinDiff(nombres)