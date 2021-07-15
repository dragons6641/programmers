import math;

def rotateClockwise(matrix : list, r1 : int, c1 : int, r2 : int, c2 : int) -> int:
    (minNum, tmpNum) = (matrix[r1][c1], matrix[r1][c1]);
    
    # print(tmpNum);
    
    for curR in range(r1, r2):
        (minNum, matrix[curR][c1]) = (min(minNum, matrix[curR + 1][c1]), matrix[curR + 1][c1]);
        
    for curC in range(c1, c2):
        (minNum, matrix[r2][curC]) = (min(minNum, matrix[r2][curC + 1]), matrix[r2][curC + 1]);
        
    for curR in range(r2, r1, -1):
        (minNum, matrix[curR][c2]) = (min(minNum, matrix[curR - 1][c2]), matrix[curR - 1][c2]);
        
    for curC in range(c2, c1 + 1, -1):
        (minNum, matrix[r1][curC]) = (min(minNum, matrix[r1][curC - 1]), matrix[r1][curC - 1]);
        
    matrix[r1][c1 + 1] = tmpNum;
    
    return minNum;

def solution(rows, columns, queries):
    answer = [];
    matrix = [[(r * columns) + c for c in range(1, columns + 1)] for r in range(0, rows)];
    
    for (r1, c1, r2, c2) in queries:
        answer.append(rotateClockwise(matrix, r1 - 1, c1 - 1, r2 - 1, c2 - 1));
    
    # print(matrix);
    
    return answer;
