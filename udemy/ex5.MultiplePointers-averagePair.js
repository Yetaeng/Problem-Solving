// Time: O(N), Space: O(1)
function averagePair(arr, avg) {
    if (arr.length < 2) return false;

    const double = avg * 2;
    for (let i=0; i<arr.length; i++) {
        let rest = double - arr[i];
        if (rest in arr) {
            return true;
        }
    }
    return false;
}
// 멀티포인터 이용해서 풀었어야 했는데, 그냥 풀어버렸넹,,,

function averagePairSol(arr, num) {
    let start = 0
    let end = arr.length - 1;
    while (start < end) {
        let avg = (arr[start] + arr[end]) / 2
        if (avg === num) return true;
        else if (avg < num) start++
        else end--
    }
    return false;
}

console.log(averagePair([], 4));
console.log(averagePair([1,3,3,5,6,7,10,12,19], 8));