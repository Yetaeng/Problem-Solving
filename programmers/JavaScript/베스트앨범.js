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