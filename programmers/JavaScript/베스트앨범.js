function solution(genres, plays) {
  let answer = [];
  
  // 고유번호: 재생수
  let plays_obj = {};
  plays.forEach((v,i) => {
      plays_obj[i] = plays[i]
  });
  
  // 장르: 고유번호
  let genres_obj = {};
  genres.forEach((v,i) => {
      if (genres_obj[v]) {
          genres_obj[v].push(i)
      } else {
          genres_obj[v] = [i]
      }
  });

  if (Object.keys(genres_obj).length === 1) {
      let key = Object.keys(genres_obj).toString();
      genres_obj[key].sort((b,a) => {
          a = plays_obj[a];
          b = plays_obj[b];
          return a-b;
      })
  }

  // 많이 재생된 순서로 정렬한 장르: 고유번호
  Object.entries(genres_obj).sort((b,a) => {
      a = a[1].sort((b,a) => {
          a = plays_obj[a];
          b = plays_obj[b];
          return a-b;
      });
      b = b[1].sort((b,a) => {
          a = plays_obj[a];
          b = plays_obj[b];
          return a-b;
      });
  });
  
  // 장르 : 재생수 (장르 우선순위 구하기 위함)
  let genres_plays = {};
  genres.forEach((v,i) => {
      if (genres_plays[v]) {
        genres_plays[v].push(plays[i])
      } else {
        genres_plays[v] = [plays[i]]
      }
  });

  const sorted = Object.entries(genres_plays).sort(([,a], [,b]) => {
      a = a.reduce((sum, curr) => sum+curr);
      b = b.reduce((sum, curr) => sum+curr);
      return b - a;
  });
  
  let genres_order = [];
  for (const [k, v] of Object.entries(sorted)) {
      genres_order.push(v[0]);
  };
  
  for (let v of genres_order) {
      let len = genres_obj[v].length === 1 ? 1 : 2;
      for (let i=0; i<len; i++) {
          answer.push(genres_obj[v][i])
      }
  }

  return answer;
}

// 다른 사람의 풀이 : 메소드 활용 대단하다
function solution2(genres, plays) {
  let obj_totalCnt = {};
  genres.forEach((v, i) => {
    obj_totalCnt[v] = obj_totalCnt[v] ? obj_totalCnt[v] + plays[i] : plays[i];
  }); //	{ classic: 1450, pop: 3100 }

  let dup_obj = {};
  const answer = genres
                  .map((v,i) => ({genre: v, play: plays[i], index: i}))
                  .sort((a,b) => {
                    if (a.genre !== b.genre) return obj_totalCnt[b.genre] - obj_totalCnt[a.genre]; // 장르가 다르면 총 재생수 기준으로 내림차순 정렬
                    if (a.play !== b.play) return b.play - a.play; // 각 노래마다 재생수 기준으로 내림차수 정렬
                    return a.index - b.index; // 그 외에는 고유번호가 빠른순으로 정렬
                  })
                  .filter(s => {
                    if (dup_obj[s.genre] >= 2) return false; // 필터된 요소들 순서대로 dup_obj에 넣을 때 2개 이상이 되면 필터링 멈추기 위함 
                    dup_obj[s.genre] = dup_obj[s.genre] ? dup_obj[s.genre] + 1 : 1;
                    return true;
                  })
                  .map(v => v.index)

  return answer;
}