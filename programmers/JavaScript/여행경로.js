// Lv.3
function solution(tickets) {
  let answer = [];
  let route = [];
  let visited = [];
  let tickets_n = tickets.length;
  tickets.sort();

  dfs('ICN', 0);

  function dfs(depart, cnt) {
    console.log('---', depart, route, cnt);
    route.push(depart);

    // 탈출 조건
    if (cnt === tickets_n) {
      answer = route;
      return route;
    }

    for (let i=0; i<tickets_n; i++) {
      if (tickets[i][0] === depart && !visited[i]) {
        visited[i] = true;
        let newDepart = tickets[i][1];
        console.log(newDepart);
        if (dfs(newDepart, cnt + 1)) return true; // 계속 탐색할 수 있으면 true 리턴

        visited[i] = false; // 못하면 현재 노드의 방문처리를 취소함
      }
    }

    route.pop(); // 유효지점이 아니라면 빼냄
    return false;
  }

  return answer;
}

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]];
console.log(solution(tickets));