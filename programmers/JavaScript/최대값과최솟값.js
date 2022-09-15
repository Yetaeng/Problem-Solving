function solution(s) {
    const arr = s.split(" ");
    arr.sort((a,b) => {return a-b});
    arr.splice(1, arr.length-2);
    
    return arr.join(" ");
}