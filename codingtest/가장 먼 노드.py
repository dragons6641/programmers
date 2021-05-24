import collections;

def solution(n, edge):
    answer = 0;
    maxDist = -1;
    isVisited = [False for i in range(n + 1)];
    
    """
    isConnected = [[False for col in range(n + 1)] for row in range(n + 1)];
    
    dq = collections.deque();
    
    isVisited[1] = True;
    
    for (src, dst) in edge:
        isConnected[src][dst] = True;
        isConnected[dst][src] = True;
    
    # print(isVisited);
    # print(isConnected);
    
    dq.append([1, 0]);
    
    while (dq):
        (curIdx, curDist) = dq.popleft();
        
        if (maxDist == curDist):
            answer += 1;
        elif (maxDist < curDist):
            answer = 1;
            maxDist = curDist;
        
        # print(curNode);
        
        for nextIdx in range(1, n + 1):
            if ((isVisited[nextIdx]) or (not isConnected[curIdx][nextIdx])):
                continue;
            
            isVisited[nextIdx] = True;
            dq.append([nextIdx, curDist + 1]);
    """
    
    adjacencyList = [[] for i in range(n + 1)];
    
    dq = collections.deque();
    
    isVisited[1] = True;
    
    for (src, dst) in edge:
        adjacencyList[src].append(dst);
        adjacencyList[dst].append(src);
    
    # print(isVisited);
    # print(adjacencyList);
    
    dq.append([1, 0]);
    
    while (dq):
        (curIdx, curDist) = dq.popleft();
        
        if (maxDist == curDist):
            answer += 1;
        elif (maxDist < curDist):
            answer = 1;
            maxDist = curDist;
        
        # print(curNode);
        
        for nextIdx in adjacencyList[curIdx]:
            if (isVisited[nextIdx]):
                continue;
            
            isVisited[nextIdx] = True;
            dq.append([nextIdx, curDist + 1]);
    
    return answer;
