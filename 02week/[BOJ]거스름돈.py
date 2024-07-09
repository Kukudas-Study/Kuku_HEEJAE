# 잔돈 500엔, 100엔, 50엔, 10엔, 5엔, 1엔
# 적은 잔돈의 개수를 만들려면 큰 금액의 잔돈순으로 계산
money=[500,100,50,10,5,1]
pay_money=int(input())
cnt=0
# 돌려받을 돈
ch_money=1000-pay_money
# 돌려받을 돈에서 큰 금액의 잔돈 순으로 빼면서 반복
# 받은 잔돈 개수 추가
for c in money:
    cnt += ch_money//c
    ch_money %=c

print(cnt)
