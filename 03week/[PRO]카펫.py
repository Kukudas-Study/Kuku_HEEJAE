def solution(brown, yellow):
    answer = []
    # 총 격자 수 = 카펫의 가로 * 세로 
    # 카펫의 가로, 세로는 총 격자 수의 약수
    total = brown + yellow
    
    for w in range(1, total+1):
        # 약수이므로 나누어서 떨어짐
        # 가로 : w, 세로 : h
        if total % w ==0:
            h = total// w
            # 제한사항
            if w>=h:
                # 카펫 테두리 1줄은 갈색 격자로 채워져 있기때문에
                if brown==((w+h)*2-4):
                    answer=[w,h]
    
    return answer
