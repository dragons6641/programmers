# 프렌즈4블록

def solution(m, n, board):
    answer = 0;
    new_board = [];

    # 새로운 배열 만들기
    for i in range(m):
        new_board.append(list(board[i]));

    while (True):
        # 지울 곳 표시할 배열
        check = [[False] * n for i in range(m)];

        # 프로그램 종료 확인
        isFinished = True;

        # 1. 지우기
        for row in range(m - 1):
            for col in range(n - 1):
                # 동, 동남, 남 다 확인해서 같으면
                # 단 공백은 아니여야 한다!
                if ((new_board[row][col] != ' '
                        and new_board[row][col] == new_board[row][col + 1])
                        and (new_board[row][col] == new_board[row + 1][col])
                        and (new_board[row][col] == new_board[row + 1][col + 1])):
                    # 지울 것으로 체크
                    isFinished = False;
                    check[row][col] = True;
                    check[row][col + 1] = True;
                    check[row + 1][col] = True;
                    check[row + 1][col + 1] = True;

        # 만약 지울 것 없으면 종료
        if (isFinished):
            break;

        # 실제로 지우자
        for row in range(m):
            for col in range(n):
                # 지워야 하는 블록이면
                if (check[row][col] == True):
                    # 공백으로
                    new_board[row][col] = ' ';
        
        # 2. 내리기
        for row in range(m):
            for col in range(n):
                # 공백 나오면
                if (new_board[row][col] == ' '):
                    for r in reversed(range(row)):
                        # 위에 있는 것 한 칸씩 아래로
                        new_board[r + 1][col] = new_board[r][col];
                        
                        # 그 자리에는 공백
                        new_board[r][col] = ' '

    # 비어있는 칸 확인 후 정답 결정
    for row in range(m):
        for col in range(n):
            # 공백만큼 지워진 것!
            if (new_board[row][col] == ' '):
                answer += 1;

    return answer;

"""
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"];
new_board = [];

# 새로운 배열 만들기
for i in range(4):
    new_board.append(list(board[i]));

print(new_board);
"""
