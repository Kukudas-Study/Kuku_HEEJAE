import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
  
    # 범위를 만족하고, 배추가 있을 경우
    if 0<=x<n and 0<=y<m:
        if graph[x][y]==1:
            # 방문 배추를 0으로 표시 -> 또 방문하지 않도록 방지
            graph[x][y] = 0
    
            # 동서남북
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)

# 테스트케이스 입력받음
T = int(input())
result_arr = []

# 각 테스트 케이스마다 배추 밭의 가로, 세로 길이와 배추 개수 입력받음
# m : 가로, n: 세로 , k : 배추 개수
# graph : 배추 밭 , result : 필요한 배추흰지렁이 수
for _ in range(T):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    result = 0
   
    # 배추 위치 입력 받아서 배추 밭(graph)에 표시
    # 배추 X : 0 , 배추 O : 1로 표시
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1
   
    # 배추 밭을 돌면서 배추가 있을 경우에
    # 인접한 배추를 탐색하고, 배추흰지렁이 수 증가
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i, j)
                result += 1
    # 각 테스트 케이스 결과 추가
    result_arr.append(result)
   
# 모든 테스트 케이스 결과 출력
for result in result_arr:
    print(result)

