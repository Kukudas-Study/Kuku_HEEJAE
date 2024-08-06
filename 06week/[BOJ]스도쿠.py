# 가로(행)에 중복되는 값이 있는 지 체크
def row(r, val):
    if val in sudoku[r]:
        return False
    return True

# 세로(열)에 중복되는 값이 있는 지 체크
def col(c, val):
    for i in range(9):
        if sudoku[i][c]==val:
            return False
    return True

# 3x3 정사각형에 중복되는 값이 있는 지 체크
def square(r, c, val):
    start_r = r//3 * 3
    start_c = c//3 * 3
    for i in range(3):
        for j in range(3):
            if sudoku[start_r+i][start_c+j]==val:
                return False
    return True

def dfs(val):
    # 값을 다 채웠으면 출력
    if val == len(zeros):
        for i in range(9):
            print(*sudoku[i])
        exit()
   
    # 비어 있는 곳에 1~9까지 넣어보기
    for i in range(1, 10):
        # 값이 비어 있는 셀
        r = zeros[val][0]
        c = zeros[val][1]

        if row(r, i) and col(c, i) and square(r, c, i):
            # 숫자 넣기
            sudoku[r][c] = i
            dfs(val+1)
            # 다시 비어 있는 값으로 표시
            sudoku[r][c] = 0

# 스도쿠판 입력 받기
sudoku = [list(map(int, input().split())) for _ in range(9)]
# 비어 있는 곳 리스트
# 비어 있는 값(0)의 좌표 저장
zeros = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j]==0:
            zeros.append([i,j])
dfs(0)
