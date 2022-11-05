function solution(participant, completion) {
  let obj = {};
  for (let v of participant) {
      obj[v] = obj[v] ? obj[v] + 1 : 1;
  }
  for (let v of completion) {
      obj[v] -= 1;
  }
  for (let v of Object.entries(obj)) {
      if (v[1] === 1) return v[0]
  }
}

// 다른 사람 풀이
function solution2(participant, completion) {
    let dic = completion.reduce((obj, t)=> (obj[t]= obj[t] ? obj[t]+1 : 1 , obj) ,{}); // 초기값을 빈 객체로 줌 ex.{"완주자":1}
    return participant.find(t=> {
        if(dic[t])
            dic[t] = dic[t]-1;
        else 
            return true; // dic[t]가 undefined(완주x) 또는 0(동명이인)이 나오면 else문을 타므로 그때 t를 리턴
    });
};