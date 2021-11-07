#python program using the List slicing approach to rotate array
def rotateList(arr, d, n):
    arr[:] = arr[d:n]+arr[0:d]
    return arr

    print(arr)
    print("Rotated list is")
    print(rotateList(arr,2,len(arr)))
    