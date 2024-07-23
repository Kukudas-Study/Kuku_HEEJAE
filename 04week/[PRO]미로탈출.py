from collections import deque

def bfs(s,e,maps):
    # 상하좌우
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    # n: 세로 , m: 가로 
    n = len(maps)
    m = len(maps[0])
    # 방문 여부 -> 0: 방문 X, 1: 방문
    visited = [[0] * m for _ in range(n)]
    queue = deque()
    # 시작지점 찾았는지 -> True: 찾음 , False : X
    flag=False
    # 시작지점 찾아서 큐에 추가, 방문 표시, 시작지점 찾았는지 표시
    for i in range(n):
        for j in range(m):
            if maps[i][j] == s:
                queue.append((i,j,0))
                visited[i][j] = 1
                flag=True
                break        
        if flag:
            break
    # 큐가 빌 때까지 반복해서 큐에서 좌표와 현재걸린시간(cnt)을 하나씩 꺼냄
    while queue:
        x,y,cnt = queue.popleft()
        # 출구에 도착했을 때
        if maps[x][y] == e:
            return cnt
        # 4개 방향 탐색
        for t in range(4):
            ny = y + dy[t]
            nx = x + dx[t]
            # 범위 안에 있고, 벽이 아니고, 방문하지 않은 경우일때
            # 시간 증가하고 큐에 추가, 방문 표시
            if 0 <= nx < n and 0 <= ny < m :
                if maps[nx][ny]!='X'and visited[nx][ny] == 0:
                    queue.append((nx,ny,cnt+1))
                    visited[nx][ny] = 1
    return -1

def solution(maps):
    answer = 0
    # 시작지점부터 레버까지 최단 거리
    first = bfs('S','L',maps)
    # 레버부터 출구까지 최단거리
    second = bfs('L','E',maps)
    # 2개의 최단거리 합
    if first != -1 and second != -1:
        answer=first+second
        return answer
    
    return -1

