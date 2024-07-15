# n : 카드 개수 , m : 딜러가 외친 숫자
n, m=map(int, input().split())
# n장의 카드
card_list=list(map(int,input().split()))
# 카드 세장의 합 중 최댓값 넣을 변수 초기화
sum=0
# n장의 카드 중 3개 뽑기
for i in range(n-2):
    for j in range(i+1,n-1):
        for p in range(j+1,n):
            # 뽑힌 카드 3장의 숫자 합계
            ex_sum=card_list[i]+card_list[j]+card_list[p]
            # 딜러가 외친 숫자를 넘지 않을 경우
            # 그 중에 가장 큰 합계 구하기
            if ex_sum<=m:
                sum=max(sum,ex_sum)
print(sum)

