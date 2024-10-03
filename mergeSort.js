let arr = [6,3,4,1,5,2,7,0]
let n = arr.length

function checkSorted(arr){
    let count = 0
    for(i = 1; i< n; i++){
        if(arr[i] > arr[i-1]){
            count ++
            if(count == n-1){
                return true
            }
        else return false
        }
    }
}

function findMiddle(arr){
    let firstIndex = arr[0]
    let lastIndex = arr[(arr.length) -1]
    let middle = (firstIndex+ lastIndex)/2
    return Math.floor(middle)
}


function mergeSort(arr){
    if (checkSorted(arr))
        return true
    findMiddle(arr)
    

}

mergeSort(arr)