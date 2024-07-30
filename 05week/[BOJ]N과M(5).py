n,m = map(int,input().split())
nlist=list(map(int,input().split()))
# 리스트 정렬 -> 결과가 사전 순으로 출력해야 하므로
nlist.sort()
arr=[]
def back():
    # 길이가 m일 때 출력
    # 문자열로 변환하고, 공백으로 구분해 출력
    if len(arr)==m:
        print(' '.join(map(str,arr)))
        return
   
    # nlist 순회하며 arr에 i가 포함되지 않으면
    # 리스트에 추가하고, back()호출, 리스트 비우기
    for i in nlist:
        if i not in arr:
            arr.append(i)
            back()
            arr.pop()
# 백트래킹 시작            
back()
