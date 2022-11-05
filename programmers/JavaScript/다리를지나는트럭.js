function solution(bridge_length, weight, truck_weights) {
    let time = 1;
    const trucks = truck_weights.length;
    let passed = [];
    let queue = [];
    
    let obj = {};
    obj[time] = truck_weights[0];
    queue.push(truck_weights.shift());
    
    // weight 10단위로 끊어서 키 값주기 (10,000 이하)
    let sum;
    while (passed.length !== trucks) {
            Object.keys(obj).find(v => {
                if (time == bridge_length + parseInt(v)) {
                    passed.push(queue.shift());
                }
            });
            
            sum = queue.reduce((sum, curr) => sum+curr, 0);
            if (sum + truck_weights[0] <= weight) {
                obj[time] ? obj[time+1] = truck_weights[0] : obj[time] = truck_weights[0]; 
                queue.push(truck_weights.shift());
            }
            time++
    }

    return time-1;
}

// console.log(solution(2, 10, [7,4,5,6]));
// console.log(solution(100, 100, [10]));
// console.log(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]));