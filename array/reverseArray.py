def reverseArray(arr):
    if len(arr) < 1:
        return arr
    a, b = 0, len(arr) - 1
    for n in range(len(arr)//2):
        if a < b:
            arr[a],arr[b] = arr[b], arr[a]
            a += 1
            b -= 1
    
    return arr



arr = [1,2,3,4]
arr2 = [1,2,3,4,5]
arr3 = [1,2,3,4,5,6]
arr4 = [1,2,3,4,5,6,7]
arr5 = []
arr6 = [1]

print(reverseArray(arr))
print(reverseArray(arr2))
print(reverseArray(arr3))
print(reverseArray(arr4))
print(reverseArray(arr5))
print(reverseArray(arr6))