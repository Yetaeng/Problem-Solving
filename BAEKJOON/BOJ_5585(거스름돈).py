changes = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]
cnt = 0

for coin in coins:
    q, r = divmod(changes, coin)
    cnt += q
    changes = r
print(cnt)

# Python3로 하면 29380KB 64ms
# PyPy3로 하면 121808KB 152ms
