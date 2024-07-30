n,m = map(int,input().split())
nlist=list(map(int,input().split()))
# 리스트 정렬 -> 결과가 사전 순으로 출력해야 하므로
nlist.sort()
arr=[]
#방문 리스트-> 방문 : 1, 방문 X : 0
visited=[0 for _ in range(n)]
def back():
    # 길이가 m일 때 출력
    # 문자열로 변환하고, 공백으로 구분해 출력
    if len(arr)==m:
        print(' '.join(map(str,arr)))
        return
    # 중복되는 것을 방지하기 위해 현 숫자 넣기 위한 변수
    num=0
    # nlist를 순회하며
    # 이전 숫자와 현 숫자가 일치하지 않고, 방문하지 않은 경우
    for i in range(n):
        if num != nlist[i] and not visited[i]:
            # 방문 처리하고 리스트에 추가하고, n에 현 숫자로 업데이트
            visited[i]=1
            arr.append(nlist[i])
            num=nlist[i]
            # back()호출, 방문상태 초기화, 리스트 비우기
            back()
            visited[i]=0
            arr.pop()
# 백트래킹 시작
back()
