// 두 정수가 같은 빈도의 숫자를 가지는지 O(N)
function sameFrequency(num1, num2) {
    const arr1 = Array.from(String(num1));
    const arr2 = Array.from(String(num2));

    if (arr1.length !== arr2.length) {
        return false;
    }

    let obj1= {};
    for (let x of arr1) {
        obj1[x] = (obj1[x] || 0) +1 ;
    }
    for (let x of arr2) {
        obj1[x] = (obj1[x] || 0) -1 ;
        if (obj1[x] < 0) {
            return false;
        }
    }

    return true;
}

console.log(sameFrequency(182, 284))
