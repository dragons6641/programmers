def solution(n, times):
    answer = 0;
    left = min(times);
    right = max(times) * n;
    
    # times.sort();
    
    # print(times);
    
    while (left <= right):
        immigrationCnt = 0;
        mid = (left + right) // 2;
        
        for time in times:
            immigrationCnt += (mid // time);
            
            if (immigrationCnt >= n):
                break;
        
        if (immigrationCnt < n):
            left = mid + 1;
        else:
            answer = mid;
            right = mid - 1;
    
    return answer;
