n, m = map(int, input().split())
arr = []

def back():
    # 길이가 m일 때 출력
    # 문자열로 변환하고, 공백으로 구분해 출력
    if len(arr) == m:
        print(" ".join(map(str, arr)))
        return
    # 1~n까지 순회하며 arr에 i가 포함되지 않으면
    # 리스트에 추가하고, back()호출, 리스트 비우기
    for i in range(1, n+1):
        if i not in arr:
            arr.append(i)
            back()
            arr.pop()
# 백트래킹 시작
back()
