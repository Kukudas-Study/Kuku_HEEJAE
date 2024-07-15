def solution(numbers, target):
    answer = 0
    # index : numbers의 인덱스, sum : 현 합계, cnt : 경우의 수
    index=0
    sum=0
    cnt=0
    
    # DFS 방식
    def dfs(index, sum):
        # 외부에 선언된 cnt 변수 사용
        nonlocal cnt
        # numbers 원소를 다 사용했을 때
        # 현 합계와 target이 같으면 경우의 수 증가
        if index ==len(numbers):
            if sum==target:
                cnt +=1
            return
        # numbers 원소가 남았을 때
        # 해당 index의 숫자를 더하거나 빼는 경우
        else:   
            dfs(index+1, sum+numbers[index])
            dfs(index+1, sum-numbers[index])
        return cnt

    answer=dfs(index,sum)
    return answer

