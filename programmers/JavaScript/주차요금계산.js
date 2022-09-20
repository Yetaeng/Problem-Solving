function solution(fees, records) {
    const cars = new Object();
    const totalParkingTime = new Object();
    for (let v of records) {
        let number = v.split(" ")[1];
        if (!cars[number]) {
            cars[number] = [v.split(" ")[0]]
        } else {
            cars[number].push(v.split(" ")[0])
        }
    }


    for (const [key, value] of Object.entries(cars)) {
        value.sort((a,b) => {return -1});

        let n = value.length;
        let parkingTime = 0;
        let parkingTime2 = 0;
        let timeCalc = 0;

        while (value.length !== 0) {
            // 입출차 모두 했을때
            if (n % 2 === 0) {
                let time = value.pop().split(":");
                let hh = time[0];
                let mm = time[1];
                timeCalc = (hh*3600 + mm*60);

                // 입차
                if (value.length % 2 == 1) {
                    parkingTime -= timeCalc;
                } else { // 출차
                    parkingTime += timeCalc;
                    parkingTime2 += parkingTime;
                    parkingTime = 0;
                }
            } else { // 마지막에 출차안했을때
                let time = value.pop().split(":");
                let hh = time[0];
                let mm = time[1];
                timeCalc = (hh*3600 + mm*60);

                if (value.length % 2 == 0) {
                    parkingTime -= timeCalc;
                    if (value.length === 0) {
                        parkingTime2 += (86340 - timeCalc);
                    }
                } else {
                    parkingTime += timeCalc;
                    parkingTime2 += parkingTime;
                    parkingTime = 0;
                    
                }
            }
        }
        totalParkingTime[key] = parkingTime2 / 60;
    }


    let [standardTime, standardFee, unitTime, unitFee] = fees;
    const feeByCar = new Object();

    for (const [key, value] of Object.entries(totalParkingTime)) {
        if (value <= standardTime) {
            feeByCar[key] = standardFee;
        } else {
            feeByCar[key] = standardFee + (Math.ceil((value - standardTime)/unitTime) * unitFee)
        }
    }

    const sorted = Object.entries(feeByCar).sort((a,b) => {
        return a[0] - b[0]
    });

    const answer = [];
    for (let v of sorted) {
        answer.push(v[1])
    }

    return answer;
}

const fees = [180, 5000, 10, 600];
const records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"];

console.log(solution(fees, records))