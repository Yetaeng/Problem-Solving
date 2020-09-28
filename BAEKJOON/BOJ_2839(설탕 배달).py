n = int(input())
sugar_bag = 0

while n > 0:
  if n % 5 != 0:
    n -= 3
    if n < 0:
      sugar_bag = -1
      break
    sugar_bag += 1
  elif n % 5 == 0:
    sugar_bag += n // 5
    n = 0
  elif n % 5 != 0 and n % 3 != 0:
    sugar_bag = -1
    break

print(sugar_bag)