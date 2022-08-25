function solution(s){
    const s_arr = s.split("");
    if ((s_arr[0] === ")") || (s_arr[s_arr.length-1] === "(")) return false;
    
    let stack = [];
    let end;
    
    while (s_arr.length !== 0) {
        end = s_arr.pop();
        stack.push(end);
        
        if (stack.length === 1 && end === '(') {
            return false;
        } else if (stack.length === 1) {
            continue;
        }
        
        if (end !== stack[stack.length-2]) {
            stack.splice(stack.length-2, 2)
        }
    }
    
    if (stack.length === 0) {
        return true;
    } else {
        return false;
    }
}