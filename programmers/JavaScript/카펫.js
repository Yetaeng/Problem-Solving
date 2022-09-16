function solution(brown, yellow) {
    const divisors = [];
    let num = brown + yellow;
    let square = Math.sqrt(num);

    if (square) {
        for (let i=1; i<=square; i++) {
            if (num % i === 0) divisors.push(i);
        }
    } else {
        for (let i=1; i<=num/2; i++) {
            if (num % i === 0) divisors.push(i);
        }
    }
    
    let col = divisors.pop();
    let row = num / col;

    while ((row-2)*(col-2) !== yellow) {
        col = divisors.pop();
        row = num / col;
    }
    
    return [row, col];
}