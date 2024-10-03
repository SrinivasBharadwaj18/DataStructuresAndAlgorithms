arr = [6,3,4,21,54,2,27,0,9]
find_item = 54


def binary_search(arr,find_item):
    middle = (0 + len(arr))//2
    arr = sorted(arr)
    i = middle
    notFound = True
    print(arr)
    if(arr[middle] == find_item):
        return middle
    if find_item< arr[middle]:
        while notFound:
            if(arr[i] == find_item):
                notFound = False
                return i
            i-=1

    elif find_item> arr[middle]:
        while notFound:
            if(arr[i] == find_item):
                notFound = False
                return i
            i+=1

index = binary_search(arr, find_item)
print(index)