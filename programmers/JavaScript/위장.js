function solution(clothes) {
  let answer = 1;
  let obj = {};
  let countedName = [];
  
  clothes.forEach((v,i) => {
      let name = v[0];
      let type = v[1];
      
      if (obj[type]) {
          obj[type].push(name)
      } else {
          obj[type] = [name]
      }
  });
  
  // 종류별 옷의 갯수
  for (let v of Object.values(obj)) {
      countedName.push(v.length);
  }
  // 옷 갯수
  let clothes_n = clothes.length;
  
  // (x+a)(x+b)(x+c) = x^3 + (a+b+c)x^2 + (ab+bc+ac)x + abc
  for (let v of countedName) {
    answer = answer * (v+1);
  }

  if (countedName.length === 1) {
    return clothes_n;
  } else {
    return answer-1
  }
}

console.log(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]));