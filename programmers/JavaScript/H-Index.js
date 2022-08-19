function solution(citations) {
  const reduceArr = citations.reduce((sum, curr) => {
    return sum + curr;
  });
  if (reduceArr === 0) return 0;
  
  const result = [];
  citations.sort((a,b) => {
    return b - a
  });
  citations.forEach((v,i) => {
    if (v >= i+1) {
      result.push(i+1);
    }
  });
  
  return result[result.length-1];
}

// h-index's def: 어떤 연구자의 h 지수는 그 사람이 쓴 모든 논문 중 n회 이상 인용된 논문이 n개 이상일 때, 이 둘을 동시에 만족하는 n의 최대값으로 한다.
// f() = max{i: f(i) >= i, i는 정수}