from collections import deque

def solution(maps):
    answer = 0
    # 맵 n x m
    n=len(maps)
    m=len(maps[0])
    # 상하좌우 
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    queue=deque()
    # 큐에 시작점 추가
    queue.append((0,0))
    # 큐가 빌 때까지 반복해서 큐에서 좌표를 하나씩 꺼냄
    while queue:
        x,y=queue.popleft()
        # 4개 방향 탐색
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            # 범위 안에 있고, 이동할 수 있는 경우
            # 이동 가능: 1, 벽 : 0
            if 0<= nx <n and 0<= ny <m:
                if maps[nx][ny]==1:
                    maps[nx][ny]=maps[x][y]+1
                    # 다음 좌표 추가
                    queue.append((nx,ny))
                    
    # 최단거리 거리
    answer = maps[n-1][m-1]
    # 진영에 도착 할 수 없을 경우
    if answer==1:
        answer=-1
    
    return answer

