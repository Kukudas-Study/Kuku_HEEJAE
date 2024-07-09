def solution(n):
    answer = ''
    # 수박을 반복하는 문자열
    str='수박'*n
    # 반복되는 수박을 입력받은 n번째 전까지(0부터 시작) 추출
    answer=str[:n]
    return answer
