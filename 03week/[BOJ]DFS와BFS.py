# node: 정점, edge: 간선, start_node: 시작할 정점 번호
node, edge, start_node= map(int, input().split())
# 행렬 0으로 초기화
graph=[[0]*(node+1) for i in range(node+1)]


# visit=[0]*(node+1)
# 방문 여부 리스트 0으로 초기화 => 0 :방문X , 1:방문O
visit = [0 for _ in range(node+1)]
visit2 = [0 for _ in range(node+1)]

for i in range(edge):
    # 두 정점 번호
    a,b=map(int, input().split())
    # 양방향 그래프이므로
    graph[a][b]=1
    graph[b][a]=1

# DFS
def dfs(start_node):
    # 방문
    visit[start_node]=1
    # 방문 노드 출력
    print(start_node,end=" ")
    # 아직 방문하지 않은 노드 중 연결되어 있는 경우
    for i in range(1, node+1):
        if visit[i]==0 and graph[start_node][i]==1:
            dfs(i)

# BFS
def bfs(start_node):
    queue=[start_node]
    # 방문
    visit2[start_node]=1
    while queue:
        # 큐 맨 앞 노드를 start_node로 설정
        start_node=queue.pop(0)
        print(start_node,end=" ")
        for i in range(1, node+1):
            if visit2[i]==0 and graph[start_node][i]==1:
                queue.append(i)
		            # 방문
                visit2[i]=1

dfs(start_node)
# 현재 출력이 end=" "로 이어져 있으니 한줄 띄기
print()
bfs(start_node)

