// productOfArray([1,2,3]) // 6
// productOfArray([1,2,3,10]) // 60

function productOfArray(arr) {
    if (arr.length === 0) {
        return 1;
    }

    let answer = arr[0]*productOfArray(arr.slice(1));
    return answer;
}

console.log(productOfArray([1,2,3,10]));

function productOfArraySol(arr) {
    if(arr.length === 0) {
        return 1;
    }
    return arr[0] * productOfArray(arr.slice(1));
}