# 잔돈 500엔, 100엔, 50엔, 10엔, 5엔, 1엔
money=[500,100,50,10,5,1]
pay_money=int(input())
cnt=0
# 돌려받을 돈
ch_money=1000-pay_money

for c in money:
    cnt += ch_money//c
    ch_money %=c

print(cnt)
