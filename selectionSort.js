let arr = [64,25,11,22,12]
let n = arr.length
let min_index
let first_index 

for(i = 0 ; i< n-1 ; i++){
    first_index = i
    let min_value = arr[i]
    for(j = i+1; j< n; j++){
        if(arr[j]< min_value){
            min_value = arr[j]
            min_index = j
        }
    }
    let temp = arr[min_index]
    arr[min_index] = arr[first_index]
    arr[first_index] = temp
}
console.log(arr)