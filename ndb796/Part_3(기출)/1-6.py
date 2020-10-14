import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))

    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times)
    
    # 먹기 위해 사용한 시간 + (현재 음식시간 - 이전 음식시간) * 남은 음식 개수 <= 방송이 중단된 시간
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(q, key = lambda x: x[1])
    return result[(k - sum_value) % length][1] # 이 부분이 이해가 안된다ㅠ
    
    # 코드가 날라가서 첨부할 순 없지만, 처음 내가 풀었던 코드는 정확도 25?에 효율성 0 이였다,,ㅠ
    # 우선순위 힙을 사용하지 않고, 그냥 선형적으로 탐색해서 그런 것 같다.
    
    
