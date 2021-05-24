minHouseCnt = 3;

def solution(money):
    answer = 0;
    houseCnt = len(money);
    
    """
    dp = [money[0], money[1]];
    
    if (houseCnt == minHouseCnt):
        return max(money);
    
    # money.append(money[0]);
    
    # print(money);
    
    for k in range(2, houseCnt):
        # print(k);
        
        if (k == houseCnt - 1):
            dp.append(max(dp[0], dp[houseCnt - 2], max(dp[1], dp[houseCnt - 3]) + money[houseCnt - 1]));
        else:
            dp.append(max(dp[k - 1], dp[k - 2] + money[k]));
    
    # print(dp);
    
    answer = max(dp);
    """
    
    if (houseCnt == minHouseCnt):
        return max(money);
    
    dpFirst = [money[0], max(money[0], money[1])];
    dpSecond = [money[1], max(money[1], money[2])];
    
    for k in range(2, houseCnt - 1):
        dpFirst.append(max(dpFirst[k - 1], dpFirst[k - 2] + money[k]));
        dpSecond.append(max(dpSecond[k - 1], dpSecond[k - 2] + money[k + 1]));
    
    # print(dpFirst);
    # print(dpSecond);
    
    answer = max(dpFirst[-1], dpSecond[-1]);
    
    return answer;
