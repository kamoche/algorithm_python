def selection(arr):
    min_index = 0
    for i in range(len(arr) - 1):
        min_index = i
        for x in range(i + 1,len(arr)):
                if arr[x] < arr[min_index]:
                    min_index = x
        if min_index != i:
             arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


print(selection([2,4,1,5,3,7,6]))

