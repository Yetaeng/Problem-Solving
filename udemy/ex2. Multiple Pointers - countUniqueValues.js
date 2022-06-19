function countUniqueValuesSelf(arr) {
    let answer = 0;
    for (let i=0, j=0; j<arr.length; j++) {
        if (arr[i] !== arr[j]) {
            arr[i+1] = arr[j];
            i++;
        }
        answer = i+1;
    }
    return answer;
}

function countUniqueValuesSol(arr){
    if(arr.length === 0) return 0;
    var i = 0;
    for(var j = 1; j < arr.length; j++){
        if(arr[i] !== arr[j]){
            i++;
            arr[i] = arr[j]
        }
    }
    return i + 1;
}

console.log(countUniqueValuesSelf([1, 2, 2, 5]));