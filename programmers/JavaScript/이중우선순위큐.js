function solution(operations) {
    let answer = [];
    let max;
    let min;
    let idx;
    
    operations.forEach((v,i) => {
        if (v.includes('I') === true) {
            answer.push(parseInt(v.split(" ")[1]))
        } else if (v.includes('D 1') === true) {
            max = Math.max(...answer)
            idx = answer.indexOf(max)
            answer.splice(idx, 1)
        } else if (v.includes('D -1') === true) {
            min = Math.min(...answer)
            idx = answer.indexOf(min)
            answer.splice(idx, 1)
        }
    })
    if (answer.length === 0) {
        return [0,0]
    }
    
    max = Math.max(...answer)
    min = Math.min(...answer)

    return [max, min];
}