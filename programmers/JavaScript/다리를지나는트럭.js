class Truck {
    constructor(weight) {
        this.weight = weight;
        this.position = 0;
    }
}

function solution(bridge_length, weight, truck_weights) {
    let truck;
    let queue_trucks = [];
    
    for (let v of truck_weights) {
        truck = new Truck(v);
        queue_trucks.push(truck);
    }
    
    let time = 0;
    let weight_on_bridge = 0;
    let leaved_truck;
    const on_bridge = [];
    const arrived = [];
    let n = truck_weights.length;

    if (getSumOfTruckWeights(truck_weights) <= weight) return truck_weights.length + bridge_length;
    
    while(queue_trucks.length !== 0) {
        leaved_truck = queue_trucks ? queue_trucks[0] : 0;
        // console.log('*', weight_on_bridge, leaved_truck.weight);

        if ((weight_on_bridge + leaved_truck.weight) < weight) {
            on_bridge.push(leaved_truck);
            weight_on_bridge += leaved_truck.weight;
            queue_trucks.shift();
            // console.log("동시", on_bridge)

        }
        console.log('@', on_bridge)
        for (let v of on_bridge) {
            v.position++;
            console.log('@@', v) // on_bridge 요소가 두개이상일때 왜 다 안돌지?
            if (v.position === bridge_length) {
                arrived.push(v);
                on_bridge.shift();
                weight_on_bridge -= v.weight;
                // time++;
            }
            // console.log('@@@', arrived, on_bridge)
        }
        time++;
        // console.log('time: ', time)
    }

    return time;
}

function getSumOfTruckWeights(trucks) {
    return trucks.reduce((sum,curr) => {return sum+curr}, 0);
}