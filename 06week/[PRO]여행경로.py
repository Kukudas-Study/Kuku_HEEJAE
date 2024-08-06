def solution(tickets):
    # 가능한 여행 경로 리스트
    answer = []
    # 티켓 사용 리스트 => 방문 : 1, 방문X : 0
    visited=[0]*len(tickets)
    
    def dfs(start,path):
        # 모든 티켓 사용 시 현재 경로 추가
        if len(tickets)+1 == len(path):
            answer.append(path)
            return
        # 모든 티켓 탐색
        for i in range(len(tickets)):
            # 현 티켓
            ticket=tickets[i]
            # 현 위치가 티켓 출발지와 일치하고
            # 해당 티켓 사용 안 한 경우
            # 티켓 사용 표시, 다음 경로 추가
            if start==ticket[0] and visited[i]==0:
                visited[i]=1
                dfs(ticket[1],path+[ticket[1]])
                # 티켓 사용 표시 복구(사용X)
                visited[i]=0
    # 항상 ICN 공항에서 출발    
    dfs("ICN",["ICN"])
    # 사전 순으로 정렬
    answer.sort()
    # 사전 순 가장 빠른 경로 반환
    return answer[0]

