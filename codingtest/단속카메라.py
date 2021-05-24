def solution(routes):
    answer = 0;
    routeCnt = len(routes);
    isVisited = [False for i in range(routeCnt)];
    
    routes.sort(key = lambda k : k[1]);
    
    # print(routes);
    
    for curIdx in range(routeCnt):
        (curIn, curOut) = routes[curIdx];
        
        if (isVisited[curIdx]):
            continue;
        
        answer += 1;
        
        for nextIdx in range(curIdx + 1, routeCnt):
            # print(curIdx, nextIdx);
            
            (nextIn, nextOut) = routes[nextIdx];
            
            if (isVisited[nextIdx]):
                continue;
            
            if (nextIn <= curOut):
                isVisited[nextIdx] = True;
    
    return answer;
