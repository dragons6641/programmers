mod = 1000000007;

def solution(m, n, puddles):
    answer = 0;
    dp = [[0 for c in range(n + 1)] for r in range(m + 1)];
    
    if (len(puddles[0]) > 0):
        for (r, c) in puddles:
            dp[r][c] = -1;
    
    for r in range(1, m + 1):
        for c in range(1, n + 1):
            if (dp[r][c] == -1):
                dp[r][c] = 0;
            elif ((r == 0) or (c == 0)):
                dp[r][c] = 0;
            elif ((r == 1) and (c == 1)):
                dp[r][c] = 1;
            else:
                dp[r][c] = (dp[r - 1][c] + dp[r][c - 1]) % mod;
    
    print(dp);
    
    answer = dp[m][n];
    
    return answer;
