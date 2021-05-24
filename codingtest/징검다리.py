def solution(distance, rocks, n):
    answer = 0;
    left = 0
    right = distance;
    
    rocks.sort();
    rocks.append(distance);
    
    # print(rocks);
    
    while (left <= right):
        prevPos = 0;
        removeCnt = 0;
        mid = (left + right) // 2;
        
        for curPos in rocks:
            if (curPos - prevPos < mid):
                removeCnt += 1;
            else:
                prevPos = curPos;
                
            if (removeCnt > n):
                break;
                
        if (removeCnt <= n):
            answer = mid;
            left = mid + 1;
        else:
            right = mid - 1;
    
    return answer;
