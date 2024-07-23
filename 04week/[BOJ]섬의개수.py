from collections import deque

# 상하좌우, 대각선 방향
dx = [1, 1, -1, -1, 1, -1, 0, 0]
dy = [0, 1, 0, 1, -1, -1, 1, -1]

def bfs(x,y):
    queue= deque()
    # 큐에 시작점 추가
    queue.append((x,y))
    # 큐가 빌 때까지 반복해서 큐에서 좌표를 하나씩 꺼냄
    while queue:
        x,y = queue.popleft()
        # 8개 방향 탐색
        for i in range(8):
            ny = y+dy[i]
            nx = x+dx[i]
            # 조건에 만족하는 방문하지 않는 육지에 방문 처리(0)하고 연결된 육지 탐색
            if 0<=ny<w and 0<=nx<h and graph[nx][ny]==1:
                graph[nx][ny]=0
                queue.append((nx,ny))

# w: 지도의 너비 , h : 지도의 높이
# graph: 지도, cnt : 섬의 개수
while True:
    w,h = map(int,input().split())
    graph = []
    cnt = 0
    if w == 0 and h == 0 :
        break
    # 지도 정보 입력
    for _ in range(h):
        graph.append(list(map(int,input().split())))
    # 육지 -> 1로 표시
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                cnt += 1
                bfs(i,j)
                
    print(cnt)
