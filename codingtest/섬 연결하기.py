def solution(n, costs):
    answer = 0;
    
    # isVisited = [False for i in range(n)];
    adjacencyMatrix = [[-1 for col in range(n)] for row in range(n)];
    
    costs.sort(key = lambda k : k[2]);
    
    # print(isVisited);
    # print(costs);
    
    """
    for (src, dst, cost) in costs:
        if ((isVisited[src]) and (isVisited[dst])):
            continue;
            
        isVisited[src] = True;
        isVisited[dst] = True;
        answer += cost;
        connectCnt += 1;
        
        if (connectCnt == n - 1):
            break;
    """
    
    for (src, dst, cost) in costs:
        adjacencyMatrix[src][dst] = cost;
        adjacencyMatrix[dst][src] = cost;

    # print(adjacencyMatrix);
    
    connectList = [costs[0][0]];
    
    for i in range(1, n):
        # print(connectCnt);
        # print(connectList);
        
        minDst = -1
        minCost = -1;
        
        for src in connectList:
            
            for dst in range(n):
                # print(src, dst);
                
                if (dst in connectList) or (adjacencyMatrix[src][dst] == -1):
                    continue;
                
                if (minCost == -1) or (minCost > adjacencyMatrix[src][dst]):
                    # print("NEXT");
                    
                    minDst = dst;
                    minCost = adjacencyMatrix[src][dst];
        
        connectList.append(minDst);
        answer += minCost;
    
    return answer;
