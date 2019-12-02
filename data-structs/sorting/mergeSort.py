# Merge sort works by splitting a list into sublists of 1 element
# And comparing elements of the left and right sublists to find
# the correct position for sorted elements
# Runtime is O(n log n)

# Implementation of Merge Sort
def sort(arr):
    # If array is length 1 it is to be merged
    # else split
    if(len(arr) > 1):
        # Find midpoint
        mid = len(arr)//2
        # Split into left and right sublists
        left = arr[:mid]
        right = arr[mid:]

        # Recursively sort on left and right
        sort(left)
        sort(right)

        i, j, k = 0, 0, 0
        # After sorting begin comparisons of sublists
        while(i < len(left) and j < len(right)):
            # If left element is smaller than or equal
            # set the arr[k] to the left element, increment sublist
            if(left[i] <= right[j]):
                arr[k]=left[i]
                i+=1
            # Else set it to the right element, increment sublist
            else:
                arr[k]=right[j]
                j+=1
            k+=1
        
        # If there are any leftover left elements add them to the list
        while i < len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        
        # If there are any leftover right elements add them to the list
        while j < len(right):
            arr[k]=right[j]
            j+=1
            k+=1
        
    return arr

print(sort([1, 3, 5, 4, 6, 9, 7, 10, 8, 2]))

