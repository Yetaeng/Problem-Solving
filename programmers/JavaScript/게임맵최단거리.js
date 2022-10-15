// Lv.2
function solution(maps) {
  let answer = 1;
  let visited = maps;
  const n = maps.length;
  const m = maps[0].length;
  const dx = [-1, 1, 0, 0];
  const dy = [0, 0, -1, 1];
  let queue = [];

  queue.push([0, 0]);
  visited[0][0] = 0;

  while (queue.length > 0) {
      let len = queue.length; // 처음 큐의 길이를 변수로 저장해서 for문을 돌려야 인접한 노드만을 방문처리함.
      // 안그러면 shift때문에 큐의 길이가 달라지므로 다음차례에 방문해야할 노드를 이전에 방문하게되는 등 문제가 발새함.

      for (let i=0; i<len; i++) {
          const [x, y] = queue.shift();
          
          for (let j=0; j<4; j++) { // 상하좌우 확인
              let nx = x + dx[j];
              let ny = y + dy[j];
              
              if (nx < 0 || ny < 0 || nx >= n || ny >= m) { // 맵 밖
                  continue;
              } else if (visited[nx][ny] == 0) { // 벽
                  continue;
              } else if (visited[nx][ny] == 1) {
                  if (nx === n-1 && ny === m-1) { // 상대팀 진영 도착
                      return ++answer;
                  }
                  queue.push([nx, ny]);
                  visited[nx][ny] = 0;
              }
          }
      }
      answer++;
  }

  return -1;
}

