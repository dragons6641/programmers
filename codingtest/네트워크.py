import collections;

isVisited = [];

def bfs(n, computers, startIdx):
    dq = collections.deque();
    
    dq.appendleft(startIdx);
    
    # print(dq);
    
    while (len(dq) > 0):
        curIdx = dq.pop();
        
        isVisited[curIdx] = True;
        
        for nextIdx in range(n):
            if (curIdx == nextIdx):
                continue;
                
            if (isVisited[nextIdx]):
                continue;
                
            if (computers[curIdx][nextIdx] == 0):
                continue;
            
            dq.appendleft(nextIdx);
    
    return;

def solution(n, computers):
    answer = 0;
    
    for i in range(n):
        isVisited.append(False);
        
    # print(isVisited);
    
    for i in range(n):
        if (not isVisited[i]):
            answer += 1;
            bfs(n, computers, i);
    
    return answer;
