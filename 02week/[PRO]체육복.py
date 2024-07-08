def solution(n, lost, reserve):
    answer = 0
    # 여벌 체육복이 있는 학생 중 빌려줄 수 있는 학생
    lend = set(reserve)-set(lost)
    # 여벌 체육복이 없어서 빌려야 하는 학생
    borrow = set(lost)-set(reserve)
    # 여벌 체육복이 있는 학생번호를 기준으로
    # 앞 번호나 뒷 번호에 체육복이 도난당한 학생이 있으면 빌려줌
    # 빌렸으면 빌려야 하는 학생들 사이에서 빼기
    for i in lend:
        if i-1 in borrow:
            borrow.remove(i-1)
        elif i+1 in borrow:
            borrow.remove(i+1)   
    # 체육복을 입을 수 있는 학생
    answer=n-len(borrow)
    
    return answer
