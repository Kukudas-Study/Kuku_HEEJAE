def solution(sizes):
    answer = 0
    
    # 가로, 세로 사이즈 저장 리스트
    width=[]
    height=[]
    
    # 명함을 가로로 눕혀서도 수납이 가능
    # 즉, 명함의 가로, 세로 길이 중 긴 길이를 가로로 생각하고
    # 작은 길이를 세로로 생각해서 리스트에 넣기
    for s in sizes:
        width.append(max(s))
        height.append(min(s))
    
    # 가로, 세로 리스트에서 가장 긴 길이끼리 곱해서
    # 모든 명함이 들어가도록 지갑 크기 지정
    answer=max(width) * max(height)
    return answer

