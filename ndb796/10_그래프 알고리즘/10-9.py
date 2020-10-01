from collections import deque
import copy  # 리스트의 경우, 단순 대입 연산을 하면 값이 변경될 수 있으므로 리스트의 값을 복제해야할 때는 deepcopy() 함수를 사용하자

v = int(input)
indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]
# 각 강의 시간을 0으로 초기화
time = [0] * (v+1)

for i in range(1, v+1):
    data = list(map(int, input().split()))  # 강의시간, 선수 강의를 차례로 입력하고, 마지막에 -1입력
    time[i] = data[0]  # i번째 강의의 시간에 입력한 정보의 첫번째 정보를 저장
    for x in data[1:-1]:  # 선수 강의 정보들을 넘겨받음
        indegree[i] += 1  # i번째 진입차수에 1을 더한다.
        graph[x].append(i)  # 정점 x에서 i로 이동 == i의 선수 강의는 x


def topology_sort():
    result = copy.deepcopy(time)  # 알고리즘 수행 결과를 담을 리스트
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph(now):
            result[i] = max(result[i], result[now] + time[i])  # 이 부분 잘 생각하기!!!
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    # n개의 강의에 대하여 수강하기까지 걸리는 최소 시간을 각각 출력
    for i in range(1, v+1):
        print(result[i])


topology_sort()

# 각 노드에 대하여 인접한 노드를 확인할 때, 인접한 노드에 대하여 현재보다 강의 시간이 더 긴 경우를 찾는다면, 그 시간 값을 저장하여 정답을 구한다.
