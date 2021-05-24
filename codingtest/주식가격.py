def solution(prices):
    timeLen = len(prices);
    answer = [0 for i in range(timeLen)];
    s = [];
    
    for curTime in range(timeLen):
        curPrice = prices[curTime]
        
        while (len(s) > 0):
            (lastTime, lastPrice) = s[-1];
        
            if (curPrice < lastPrice):
                s.pop();
                answer[lastTime] = curTime - lastTime;
                
            else:
                break;
                
        s.append([curTime, curPrice]);
        
    while (len(s) > 0):
        (lastTime, lastPrice) = s[-1];

        s.pop();
        answer[lastTime] = curTime - lastTime;
    
    return answer;
