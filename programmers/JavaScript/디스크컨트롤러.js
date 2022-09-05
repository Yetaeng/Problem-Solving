function solution(jobs) {
    let n = jobs.length;
    let total_worked_time = 0;
    let end_point = 0;
    const waiting_list = [];

    jobs.sort((a,b) => {
        if (a[0]===b[0]) {
            return a[1]-b[1]
        }
        return a[0]-b[0]
    });

    while(jobs.length !== 0 || waiting_list.length !== 0) {
        while (jobs[0] && end_point >= jobs[0][0]) {
            waiting_list.push(jobs[0]);
            jobs.shift();
        }
        
        if (waiting_list.length > 0) {
            waiting_list.sort((a,b) => {return a[1]-b[1]});
            let item = waiting_list.shift();
            total_worked_time += end_point + item[1] - item[0];
            end_point += item[1];
        } else {
            total_worked_time += jobs[0][1];
            end_point = jobs[0][0] + jobs[0][1];
            jobs.shift();
        }
    }
    
    return Math.floor(total_worked_time/n);
}