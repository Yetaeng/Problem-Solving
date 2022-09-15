function solution(n) {
    let memo = [0, 1];
    
    for (let i=2; i<=n; i++) {
        if (!memo[i]) {
            memo.push((memo[i-1]+memo[i-2]) % 1234567)
        }
    }
    
    return memo[n]; 
    
    // 마지막 단계에서 나누어주면 오버플로우가 발생하므로, 모든 단계에서 %를 사용한후 memo에 넣어준다.
    // 결합법칙
    // F(n) % m 
    // = (F(n-1) + F(n-2)) % m
    // = (F(n-1) % m + F(n-2) % m) % m
}