function solution(bridge_length, weight, truck_weights) {
    let time = 0;
    let out_truck;
    let waiting_truck;
    const on_bridge = [];
    const arrived = [];
    const truck_weights_sum = getSumOfTruckWeights(truck_weights);
    
    if (truck_weights_sum <= weight) return truck_weights.length + bridge_length;

    while(arrived.length !== truck_weights.length) {
        out_truck = truck_weights.shift();
        waiting_truck = truck_weights[0];

        for (let i=bridge_length; i>=0; i--) {
            if ((getSumOfTruckWeights(on_bridge) + waiting_truck < weight) && (on_bridge.length < bridge_length)) {
                // 다리에 트럭 추가
                if (on_bridge.length === 0) {
                    on_bridge.push(out_truck)
                } else {
                    on_bridge.push(waiting_truck);
                }
                time++;
                console.log('*', on_bridge, truck_weights, time);
            } else if ((getSumOfTruckWeights(on_bridge) + waiting_truck < weight) && (on_bridge.length === bridge_length)) {
                // 트럭이 다리를 지남
                arrived.push(on_bridge.shift());
                time++;
                console.log('**', on_bridge, truck_weights, time);
            } else if ((getSumOfTruckWeights(on_bridge) + waiting_truck >= weight) && (on_bridge.length < bridge_length)) {
                // 다리위 트럭만 이동
                time++;
                console.log('***', on_bridge, truck_weights, time);
            }
        }
        arrived.push(on_bridge.shift());

        if (on_bridge.length === 1 && truck_weights.length === 0) {
            console.log('#', on_bridge, truck_weights, time);
            return time + bridge_length;
        }
    }
    return time;
}

function getSumOfTruckWeights(trucks) {
    return trucks.reduce((sum,curr) => {return sum+curr}, 0);
}