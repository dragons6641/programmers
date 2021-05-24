maxPlayerCnt = 100;

def solution(n, results):
    answer = 0;
    
    """
    visitCnt = [0 for i in range(n + 1)];
    adjacencyMatrix = [[maxPlayerCnt for col in range(n + 1)] for row in range(n + 1)];
    
    for (src, dst) in results:
        adjacencyMatrix[src][dst] = 1;
    
    for startIdx in range(1, n + 1):
        for endIdx in range(1, n + 1):
            for stopoverIdx in range(1, n + 1):
                if (adjacencyMatrix[startIdx][endIdx] > \
                    adjacencyMatrix[startIdx][stopoverIdx] + adjacencyMatrix[stopoverIdx][endIdx]):
                    adjacencyMatrix[startIdx][endIdx] = \
                    adjacencyMatrix[startIdx][stopoverIdx] + adjacencyMatrix[stopoverIdx][endIdx];
                    
    for startIdx in range(1, n + 1):
        for dstIdx in range(1, n + 1):
            if (adjacencyMatrix[startIdx][dstIdx] < maxPlayerCnt):
                visitCnt[dstIdx] += 1;
            
    print(visitCnt);
    print(adjacencyMatrix);
    """
    
    adjacencyMatrix = [[0 for col in range(n + 1)] for row in range(n + 1)];
    
    for (src, dst) in results:
        adjacencyMatrix[src][dst] = 1;
        adjacencyMatrix[dst][src] = -1;
    
    for src in range(1, n + 1):
        for dst in range(1, n + 1):
            for mid in range(1, n + 1):
                if (adjacencyMatrix[src][mid] == 1) and (adjacencyMatrix[mid][dst] == 1):
                    adjacencyMatrix[src][dst] = 1;
                    adjacencyMatrix[dst][src] = -1;
                elif (adjacencyMatrix[src][mid] == -1) and (adjacencyMatrix[mid][dst] == -1):
                    adjacencyMatrix[src][dst] = -1;
                    adjacencyMatrix[dst][src] = 1;
                
    # print(adjacencyMatrix);
    
    for result in adjacencyMatrix:
        if (result.count(0) == 2):
            answer += 1;
    
    return answer;
