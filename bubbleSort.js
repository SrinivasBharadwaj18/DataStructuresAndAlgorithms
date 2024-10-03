let arr = [64,25,11,22,12]

for(i=0;i<arr.length-1;i++){
    for(let j = i+1; j<arr.length;j++){
        if(arr[j]<arr[i]){
            console.log(arr[j], arr[i])
            let temp = arr[i]
            arr[i] = arr[j]
            arr[j] =temp
        }
    }
    console.log(arr)
}

//key points

//1. if you use only one for loop you are sorting the array only once - that will only sort one number out of the array to the correct position
//2. so you need to do the sorting of the array n-1 times where n is the length of the array as you dont need to sort n times cause when u sort the array
// n -1 times then itself the array is getting completely sorted
// time complexity = n(n-1) = n^2 - n  = O(n^2) 