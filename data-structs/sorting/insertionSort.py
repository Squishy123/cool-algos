# Insertion Sort works by iterating through an array
# Taking each nth element, and iterating through the 0-n
# Swapping while arr[n] is > than arr[n-1]
# Runtime is O(n^2)

# Implementation of Insertion Sort
def sort(arr):
    for i in range(len(arr)):
        for j in range(i, 1, -1):
            if(arr[j] < arr[j-1]):
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

# Implementation of Insertion Sort with Recursion
def rSort(arr):
    def aux(arr, n=0):
        if(n == len(arr)):
            return arr
        
        for i in range(n, 1, -1):
            if(arr[i] < arr[i-1]):
                arr[i], arr[i-1] = arr[i-1], arr[i]
        
        return aux(arr, n+1)
    return aux(arr)

print(sort([1, 3, 5, 4, 6, 9, 7, 10, 8, 2]))
print(rSort([1, 3, 5, 4, 6, 9, 7, 10, 8, 2]))