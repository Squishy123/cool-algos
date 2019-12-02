# Implementation of Binary Search
def search(arr, val):
    def aux(arr, offset=0):
        if(arr == []):
            return -1
        mid=len(arr)//2
        if(arr[mid] == val):
            return offset+mid

        if(val < arr[mid]):
            return aux(arr[:mid], offset)
        else:
            return aux(arr[mid:], offset+mid)
    return aux(arr)

print(search([1, 2, 3, 4, 5, 6], 6))