// power(2,0) // 1 
// power(2,2) // 4 2*2
// power(2,4) // 16 2*2*2*2

function power(base, exponent) {
    if (exponent === 0) return 1;

    let answer = 1;
    while (exponent > 0) {
        answer = answer * base;
        exponent--;
    }
    return answer;
}

console.log(power(2, 0));

function powerSol(base, exponent){
    if(exponent === 0) return 1;
    return base * power(base,exponent-1);
}