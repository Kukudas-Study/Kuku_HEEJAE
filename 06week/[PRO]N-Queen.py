def q(queen, row, n):
    # cnt : 배치 가능한 방법의 수 
    cnt = 0
    # 모든 퀸이 배치되었을 경우
    if n == row:
        return 1
    
    #  퀸 배치
    for col in range(n):
        queen[row] = col
        for i in range(row):
            # 같은 열에 있는지 확인
            if queen[i] == queen[row]:
                break
            # 대각선에 있는지 확인
            if abs(queen[i]-queen[row]) == row - i:
                break
        # 충돌 없으면 다음 행에 퀸 배치
        else:
            cnt += q(queen, row + 1, n)
    # 배치 가능한 방법 수 반환
    return cnt

def solution(n):
    answer = q([0]*n,0,n)
    return answer

