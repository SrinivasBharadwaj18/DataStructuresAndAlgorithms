def merge_sort(arr, left, right):
    if left < right:
        # Find the middle point
        mid = left + (right - left) // 2
        print(f"left: {left}\n right: {right} \n middle: {mid}")
        print(arr[left:mid+1])
        print(arr[mid+1:right+1])
        # Recursively sort the first half and second half
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        
        # Merge the sorted halves
        merge(arr, left, mid, right)
    else: 
        print("OUT OF IT")

def merge(arr, left, mid, right):
    # Create temporary arrays to hold the two halves
    n1 = mid - left + 1  # Size of left half
    n2 = right - mid     # Size of right half
    
    # Create temp arrays to hold data
    left_half = arr[left:mid+1]
    right_half = arr[mid+1:right+1]
    
    # Merge the temp arrays back into arr[left..right]
    i = j = 0  # Initial index of left_half and right_half
    k = left   # Initial index of merged subarray
    
    while i < n1 and j < n2:
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1
    
    # Copy the remaining elements of left_half, if any
    while i < n1:
        arr[k] = left_half[i]
        i += 1
        k += 1
    
    # Copy the remaining elements of right_half, if any
    while j < n2:
        arr[k] = right_half[j]
        j += 1
        k += 1


arr =[5,2,9,1,6]
merge_sort(arr,0,4)
print(arr)