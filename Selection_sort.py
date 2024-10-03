arr = [64,25,11,22,12]
n = len(arr)
min_value = arr[0]

for i in range(len(arr) -1):
    first_index = i
    min_value = arr[i]
    for j in range(i+1,len(arr)):
        if(arr[j]< min_value):
            min_value = arr[j]
            min_index= j
    arr[min_index],arr[first_index]  = arr[first_index],arr[min_index]
    print(arr)