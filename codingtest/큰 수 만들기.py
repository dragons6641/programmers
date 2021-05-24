def solution(number, k):
    answer = '';
    number = list(map(int, number));
    # numberLen = len(number);
    # removeCnt = 0;
    # startIdx = 0;
    # endIdx = k;
    stack = [];
    
    # print(number);
    
    """
    while (numberIdx < numberLen - 1):
        curDigit = int(number[numberIdx]);
        nextDigit = int(number[numberIdx + 1]);
        
        if (curDigit < nextDigit):
            removeCnt += 1;
        else:
            answer += str(curDigit);
            
        numberIdx += 1;
            
        if (removeCnt == k):
            answer += number[numberIdx : : ];
            
            break;
    """
    
    """
    while (endIdx < numberLen):
        maxDigit = max(number[startIdx : endIdx]);
        
        print();
        print("idx =", startIdx, endIdx);
        print("max =", maxDigit);
        
        for curIdx in range(startIdx, endIdx):
            curDigit = number[curIdx];
            
            if (numberLen - curDigit == k - removeCnt):
                answer += ''.join(map(str, number[curIdx : : ]));
                
                return answer;
            
            print("cur =", curDigit);
            
            if (curDigit == maxDigit):
                answer += str(curDigit);
            else:
                removeCnt += 1;
        
        startIdx = endIdx;
        
        if (removeCnt == k - 1):
            endIdx = numberLen - 1;
            
            break;
        else:
            endIdx = startIdx + k - removeCnt;
    
    for curIdx in range(startIdx, endIdx):
        curDigit = number[curIdx];
        nextDigit = number[curIdx + 1];
        
        if (curDigit <= nextDigit):
            removeCnt += 1;
            answer += ''.join(map(str, number[curIdx + 1 : : ]));
            
            break;
    """
    
    for curDigit in number:
        while ((stack) and (stack[-1] < curDigit)) and (k > 0):
            k -= 1;
            stack.pop();
            
        stack.append(curDigit);
        
    # print(stack);
    # print(k);
    
    answer += ''.join(map(str, stack[ : len(stack) - k : ]));
    
    return answer;
