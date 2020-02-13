def solution(price, money):
    total = sum(price)
    if total > money:
        return -1
    else:
        return money-total