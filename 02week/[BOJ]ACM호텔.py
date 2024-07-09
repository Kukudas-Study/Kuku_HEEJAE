# 1호수부터 배정됨 => 1층 1호, 2층 1호 .. 순으로 
T = int(input())
# h : 호텔 층 수 , w : 각 층의 방 수, n : 몇 번째 손님
for i in range(T):
    h, w, n = map(int, input().split( ))

    floor_num = n % h 
    floor_room_num = (n // h) + 1

    # n 번째 손님이 호텔 층 수의 배수일 경우
    # 무조건 호텔 층 수인 층을 사용
    if floor_num == 0:
        floor_num = h
        floor_room_num -=1

    print(floor_num * 100 + floor_room_num)
