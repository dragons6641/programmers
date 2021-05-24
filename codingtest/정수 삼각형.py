def solution(triangle):
    answer = 0;
    dp = [triangle[0]];
    rows = len(triangle)
    
    for r in range(1, rows):
        tmpList = [];
        cols = len(triangle[r]);
        
        for c in range(cols):
            # print(r, c);
            
            if (c == 0):
                tmpList.append(dp[r - 1][c] + triangle[r][c]);
            elif (c == cols - 1):
                tmpList.append(dp[r - 1][c - 1] + triangle[r][c]);
            else:
                tmpList.append(max(dp[r - 1][c - 1], dp[r - 1][c]) + triangle[r][c]);
    
        dp.append(tmpList);
    
    # print(dp);
    
    answer = max(dp[-1]);
    
    return answer;
