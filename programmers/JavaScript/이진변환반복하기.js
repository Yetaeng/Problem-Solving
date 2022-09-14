function solution(s) {
    let arr = [...s];
    let n;
    let non_zero;
    let cnt = 0;
    let zero_length = 0;
    
    while (arr.length !== 1) {
        n = arr.length;
        non_zero = arr.filter(v => v !== '0').length;
        zero_length += n - non_zero;
        arr = [...non_zero.toString(2)];
        cnt++;
    }
    
    return [cnt, zero_length];
}