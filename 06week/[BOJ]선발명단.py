# c : 테스트 케이스 개수
c = int(input())

def back(cnt, sum):
    global result
    # 모든 선수의 포지션이 배정된 경우
    # 모든 선수의 능력치 합의 최댓값 계산
    if cnt == 11:
        result = max(result, sum)
        return

    # 11명의 선수
    for i in range(11):
        # 선택된 선수이거나, 능력치가 0인 경우 => pass
        if mem_visit[i]==1 or mem_power[cnt][i]==0:
            continue
        # 해당 선수 포지션에 지정 => 백트래킹해서 능력치 합계 갱신
        mem_visit[i] = 1
        back(cnt + 1, sum + mem_power[cnt][i])
        # 현 포지션에 지정해제 -> 선택되지 않은 선수
        mem_visit[i] = 0

# 테스트 케이스마다 선수들의 능력치를 입력받고
# 포지션 지정 선수 리스트 -> 지정됨 : 1, 지정 X : 0
# result : 능력치 합의 최댓값 저장 변수
for _ in range(c):
    mem_power = [list(map(int, input().split())) for _ in range(11)]
    mem_visit = [0 for _ in range(11)]
    result = 0
    # 백트래킹 시작
    back(0, 0)
    # 선수들의 능력치 합의 최댓값 출력
    print(result)
