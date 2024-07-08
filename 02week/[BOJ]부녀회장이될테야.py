T=int(input())
# k : 층 , n : 호
for i in range(T):
    k=int(input())
    n=int(input())
    # 2차원 리스트
    floor=[[0 for j in range(n)]for j in range(k+1)]

    # 0층 호수 순서대로 인원수 리스트 입력
    for p in range(n):
        floor[0][p]=p+1
        # print(floor)

    for q in range(k+1):
        for l in range(n):
            floor[q][l] += sum(floor[q-1][:l+1])

    print(floor[k][n-1])
