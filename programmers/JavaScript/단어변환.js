// Lv.3
// BFS

function solution(begin, target, words) {
  let queue = [];
  let visited = [];
  
  if (words.indexOf(target) < 0) return 0;
  
  queue.push([begin, 0]);
  
  while (queue.length > 0) {
      let [v, cnt] = queue.shift();
      if (v === target) return cnt;
      
      for (let word of words) {
          let diff = 0;
          for (let i=0; i<word.length; i++) {
              if (v[i] !== word[i]) diff++;
          }
          if (diff === 1 && visited.indexOf(word) < 0) {
              queue.push([word, ++cnt]);
              visited.push(word);
          }
      }
  }
}

console.log(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]));
