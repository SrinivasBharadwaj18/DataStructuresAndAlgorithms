import math
arr = [6,3,4,1,5,2,7,0]
n = len(arr) 
first_index = 0
last_index = len(arr) -1
middle = (first_index + last_index)/2

def CheckSorted(arr):
    count = 0
    for i in range(1,len(arr)):
        if arr[i] > arr[i-1]:
            count+=1
            if count == len(arr) -1:
                return True
        else:
            return False
        
arr_Sort =CheckSorted(arr)

def find_middle(arr):
    first_index = arr[0]
    last_index = arr[len(arr) -1]
    middle = (first_index + last_index)/2
    print(math.floor(middle))



print(arr_Sort)

def merge_sort(arr):
    sorted = CheckSorted(arr)
    if sorted == True:
        return arr
    middle = find_middle(arr)
    
    
merge_sort(arr)