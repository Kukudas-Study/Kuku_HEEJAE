from collections import deque

def solution(land):
    answer=0
    # 세로 : n, 가로 : m
    n=len(land)
    m=len(land[0])
    
    # 상하좌우
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    # result : 석유량 리스트, visited: 방문여부 -> 방문 :1 , 방문 X: 0
    result = [0 for _ in range(m)]
    visited=  [[0] * m for _ in range(n)]
    
    def bfs(x, y):
        # 시작지점 추가 및 방문 표히
        ground=[y]
        visited[x][y]=1
        cnt_oil = 1
        queue=deque()
        queue.append((x,y))
        # 큐가 빌 때까지 반복해서 큐에서 좌표를 하나씩 꺼냄
        while queue:
            x, y = queue.popleft()
            # 4개 방향탐색
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 범위 안에 있고, 석유가 있고, 방문하지 않은 경우
                if 0 <= nx < n and 0 <= ny < m :
                    if land[nx][ny] == 1 and visited[nx][ny]==0:
                        if ny not in ground:
                            ground.append(ny)
                        cnt_oil += 1
                        visited[nx][ny]=1
                        queue.append((nx, ny))
                                 
                                 
        return ground, cnt_oil
    
    # 땅 속을 돌면서 석유 탐색
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visited[i][j]==0:
                ground, cnt_oil = bfs(i, j)
                # 해당 열에 석유량 추가
                for k in ground:
                    result[k] += cnt_oil
    # 가장 많은 석유량
    answer=max(result)
    return answer
