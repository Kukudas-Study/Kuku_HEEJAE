# n : 세로 , m : 가로 , b : 인벤토리에 있는 블록 개수
n, m, b=map(int, input().split())
# 입력받은 좌표마다 땅 높이
height_ground=[]
# 땅의 최대 높이, 최소 높이 초기값
max_height=0
min_height=float('inf')
for _ in range(n):
    arr=list(map(int, input().split()))
    height_ground.append(arr)
    max_height=max(max_height,max(arr))
    min_height=min(min_height,min(arr))


# 최소 시간 초기값
min_time=float('inf')
# 입력받은 것 중 최소 높이와 최대 높이 까지
for current_h in range(min_height, max_height+1):
    inventory=b
    time=0


    for i in range(n):
        for j in range(m):
            # 블록 제거 -> 2초 걸림, 인벤토리에 블록 추가
            if height_ground[i][j]> current_h:
                inventory+=height_ground[i][j]-current_h
                time+=(height_ground[i][j]-current_h)*2
            # 블록 쌓기 -> 1초 걸림 , 인벤토리에 블록 제거
            else:
                inventory-=current_h-height_ground[i][j]
                time +=(current_h-height_ground[i][j])
    # 인벤토리가 음수가 아니고, 최소 시간일 때
    if inventory>=0 and time <=min_time:
        min_time=time
        result_h=current_h
print(min_time, result_h)
