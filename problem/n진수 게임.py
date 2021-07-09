DIGIT = 10;
BIAS = ord("A");

def getStrDigit(intDigit : int) -> str:
    return (str(intDigit) if (intDigit < DIGIT) else (chr(intDigit - DIGIT + BIAS)));

def solution(n, t, m, p):
    (answer, totalStr, curNum) = ('', '0', 0);
    
    for curNum in range(t * m):
        tmpStr = '';
        
        while (curNum > 0):
            tmpStr += getStrDigit(curNum % n);
            curNum = curNum // n;
            
        totalStr += tmpStr[ : : -1];
        
        if (len(totalStr) >= t * m):
            break;
    
    for chIdx in range(len(totalStr)):
        if (chIdx % m != p - 1):
            continue;
        
        answer += totalStr[chIdx];
        
        if (len(answer) == t):
            break;
    
    # print(totalStr);
    # print(answer);
    
    return answer;
