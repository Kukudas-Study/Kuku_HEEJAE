T=int(input())
# k : 층 , n : 호
for i in range(T):
    k=int(input())
    n=int(input())
    # 2차원 리스트에 0으로 초기화
    floor=[[0 for j in range(n)]for j in range(k+1)]

    # 0층 호수 순서대로 인원수 리스트 입력
    # 0층 => n호수는 n명 거주
    for p in range(n):
        floor[0][p]=p+1
        # print(floor)
    # 1층부터는 아래층에 1호수부터 자신의 호수까지 거주 인원의 합계만큼 거주
    # 인원수의 합을 구해서 리스트에 입력
    for q in range(k+1):
        for l in range(n):
            floor[q][l] += sum(floor[q-1][:l+1])

    print(floor[k][n-1])
