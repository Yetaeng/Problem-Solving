function solution(distance, scope, times) {
  let answer = distance;
  const sorted = scope.map(v => {
      if (v[0] > v[1]) return v.sort();
      else return v;
  });
  let guardStart, guardEnd, workTime, restTime, curr;
  
  for (let i=0; i<sorted.length; i++) {
      guardStart = sorted[i][0];
      guardEnd = sorted[i][1];
      workTime = times[i][0];
      restTime = times[i][1];
      
      for (let j=guardStart; j<guardEnd+1; j++) {
          curr = j % (workTime + restTime);
          
          if (0 < curr && curr <= workTime) {
              answer = Math.min(answer, j);
              break;
          }
      }
  }
  return answer;
}