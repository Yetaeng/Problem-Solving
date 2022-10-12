// Lv.1
function solution(survey, choices) {
    const types = {
        'R': 0, 'T': 0,
        'C': 0, 'F': 0,
        'J': 0, 'M': 0,
        'A': 0, 'N': 0,
    };
    let answer = [];
    let idx = 0;
    
    for (let i=idx; i<survey.length; i++) {
        if (choices[i] > 4) {
            types[survey[i][1]] += choices[i] - 4;
        } else if (choices[i] < 4) {
            types[survey[i][0]] += 4 - choices[i];
        } else {
            continue;
        }
        idx++;
    }
    
    let type, a_type, b_type, a, b;
    for (let i=0; i<8; i+=2) {
        a_type = Object.entries(types)[i][0];
        a = Object.entries(types)[i][1];
        b_type = Object.entries(types)[i+1][0];
        b = Object.entries(types)[i+1][1];
        
        type = a > b ? a_type : b_type;
        if (a === b) {
            type = a_type > b_type ? b_type : a_type;
        }
        
        answer.push(type);
    }
    
    return answer.join('');
}