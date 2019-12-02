# Shell sort works by performing insertion sort on an array
# Taking elements by a gap and decreasing the gap until it is 0
# Runtime is between O(n) and O(n^2)

# Implementation of Shell Sort
def sort(arr):
    sublistSize = len(arr)//2

    while(sublistSize > 0):
        for start in range(sublistSize):
            gapInsertionSort(arr, start, sublistSize)
        
        sublistSize = sublistSize//2
    
    return arr

# Helper function performs insertion sort on 
# elements of a certain gap
def gapInsertionSort(arr, start, gap):
    for i in range(start, len(arr), gap):
        for j in range(i, 1, -1):
            if(arr[j] < arr[j-1]):
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

print(sort([1, 3, 5, 4, 6, 9, 7, 10, 8, 2]))