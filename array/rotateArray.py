def rotate_arraY(arr):
    return list(zip(*arr[::-1]))


def rotate_array_v1(arr):
    if len(arr) == 0 or len(arr) != len(arr[0]):
        return False
    
    n = len(arr)
    for layers in range(n//2):
        first = layers
        last = n - 1 -layers
        for index in range(first, last):
            offset = index - first
            temp = arr[first][index]
            arr[first][index] = arr[last - offset][first]
            arr[last - offset][first] =arr[last][last -offset]
            arr[last][last -offset] = arr[index][last]
            arr[index][last] = temp
    return True

        


def printArray(arr):
    for i in range(len(arr)):
        print(arr[i])



arr = [[1,2,3],[4,5,6],[7,8,9]]


printArray(arr)
rotate_array_v1(arr)
print("v2=========>")
printArray(arr)
# arr = rotate_arraY(arr)
# print("=============")
# printArray(arr)
