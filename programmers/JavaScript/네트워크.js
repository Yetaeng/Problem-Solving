function solution(n, computers) {
  let answer = 0;
  let visited = [];
  
  function dfs(idx) {
      visited[idx] = true;
      for (let i=0; i<computers[idx].length; i++) {
          if (computers[idx][i] === 1 && !visited[i]) {
              dfs(i);
          }
      }
  }
  
  for (let i=0; i<n; i++) {
    // 해당 영역을 지나간 적이 없으면 재귀 호출
    if (!visited[i]) {
        dfs(i); // 연결이 안되어 있어 false라고 한다면 DFS 탈출 후 answer 카운트
        answer++;
    }
  }

  return answer;
}