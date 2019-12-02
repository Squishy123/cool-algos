# Selection Sort works by removing the min element of the array 
# And putting it into a new sorted array
# Runtime is O(n^2)

# Implementation of Selection Sort
def sort(arr):
    selected=[]
    while(len(arr) > 0):
        minVal=arr[0]
        minIndex=0
        for i in range(len(arr)):
            if(arr[i] > minVal):
                minVal=arr[i]
                minIndex=i

        selected=[arr[minIndex]]+selected 
        arr.pop(minIndex)
    
    return selected

# Recursive Implementation of Selection Sort
def rSort(arr):
    def aux(arr, acc=[]):
        if(arr == []):
            return acc

        minVal=arr[0]
        minIndex=0
        for i in range(len(arr)):
            if(arr[i] > minVal):
                minVal=arr[i]
                minIndex=i
        acc=[arr[minIndex]]+acc 
        arr.pop(minIndex)

        return aux(arr, acc)
    return aux(arr)

print(sort([1, 3, 5, 4, 6, 9, 7, 10, 8, 2]))
print(rSort([1, 3, 5, 4, 6, 9, 7, 10, 8, 2]))
