
# Quicksort works by selecting a pivot, partitioning the 2 halfs around 
# the pivot. In the partition method, use a right and left marker
# to determine the split point
# Runtime is O(n log n)

# Implementation of QuickSort
def sort(arr):
    def aux(arr, first=0, last=len(arr)-1):
        # Split as long as first and last markers are not identical or cross
        if(first < last):
            # Find split point
            splitPoint=partition(arr, first, last)

            aux(arr, first, splitPoint-1)
            aux(arr, splitPoint+1, last)
    aux(arr)
    return arr

# Partition function
def partition(arr, first, last):
    # Initial pivot value is the arr[first]
    pivotValue=arr[first]
    # Set left mark and right mark positions
    leftMark=first+1
    rightMark=last

    done=False
    while not done:
        # If left mark position is equal or less than right mark position
        # And value of arr[leftMark] is less than or equal than pivot value
        # Increment mark by 1
        while(leftMark <= rightMark and arr[leftMark] <= pivotValue):
            leftMark+=1
        
        # If right mark value is greater than or equal to pivot value
        # And right mark is to the right of or same as left mark
        # Increment mark by 1
        while(arr[rightMark] >= pivotValue and rightMark >= leftMark):
            rightMark-=1
        
        # If right mark crosses left mark, exit
        if(rightMark < leftMark):
            done=True
        # Else swap values at left and right
        else:
            arr[leftMark], arr[rightMark] = arr[rightMark], arr[leftMark]

    # Swap values of first and rightmark
    arr[first], arr[rightMark] = arr[rightMark], arr[first]   
    
    #Split point is at rightmark
    return rightMark

#print(sort([1, 3, 5, 4, 6, 9, 7, 10, 8, 2]))
print(sort([1, 3, 5, 4, 6]))