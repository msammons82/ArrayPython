
def _sum(arr):
    sum= 0



    #iterate through the array, add each element to the sum
    for i in arr:
        sum = sum + i

    return(sum)

    # driver function
    arr = []
    #input values to list
    arr = [12,3,4,15]

    # calculating length of array
    n = len(arr)

    ans = _sum(arr)

    print('Sum of the array is ',ans)