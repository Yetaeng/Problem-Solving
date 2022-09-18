function solution(s) {
    let regex = /\d+/gi;
    const matched = s.match(regex)
    const counted = countByArray(matched);
    let sorted = Object.entries(counted).sort((a, b) => b[1] - a[1]);
    let result = [];

    for (let v of sorted) {
        result.push(parseInt(v[0]))
    }
    
    return result;
}

function countByArray(arr) {
    return arr.reduce((prev, curr) => {
        prev[curr] = ++prev[curr] || 1;
        return prev;
    }, {})
}