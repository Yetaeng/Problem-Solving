// Lv.1
function solution(price, money, count) {
    let totalPrice = 0;
    for (let i=1; i<count+1; i++) {
        totalPrice += price*i;
    }
    if (totalPrice < money) return 0;
    
    return totalPrice - money;
}