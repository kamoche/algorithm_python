def bubbleSort(arr):

    for j in range(len(arr) - 1, 0, -1):
        for i in range(j):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr


print(bubbleSort([2,4,1,5,3,7,6]))
