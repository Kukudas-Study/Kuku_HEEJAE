n,m = map(int,input().split())
nlist=list(map(int,input().split()))
# 리스트 정렬 -> 결과가 사전 순으로 출력해야 하므로
nlist.sort()
arr=[]
def back(a):
    # 길이가 m일 때 출력
    # 문자열로 변환하고, 공백으로 구분해 출력
    if len(arr)==m:
        print(' '.join(map(str,arr)))
        return
    # a~n까지의 순회하며 리스트에 추가하고, back()호출, 리스트 비우기
    for i in range(a,n):
        arr.append(nlist[i])
        back(i)
        arr.pop()
# 백트래킹 시작
back(0)
