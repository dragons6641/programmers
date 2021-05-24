import collections;

isVisited = [];
isConnected = [];

def makeConnect(words, wordLen):
    # print(words, wordLen);
    # print(isConnected);
    
    for srcIdx in range(wordLen):
        srcCounter = collections.Counter(words[srcIdx]);

        for dstIdx in range(srcIdx):
            # print(srcIdx, dstIdx);
            
            dstCounter = collections.Counter(words[dstIdx]);
            
            # print(src, dst);
            # print(srcCounter - dstCounter);
            # print();
            
            if (len(srcCounter - dstCounter) == 1):
                isConnected[srcIdx][dstIdx] = True;
                isConnected[dstIdx][srcIdx] = True;

def bfs(begin, target, words, wordLen):
    dq = collections.deque();
    
    dq.appendleft([0, 0]);
    
    # print(dq);
    
    while (len(dq) > 0):
        (curIdx, curCnt) = dq.pop();
        
        # print(curIdx, curCnt);
        
        if (words[curIdx] == target):
            return curCnt;
        
        isVisited[curIdx] = True;
        
        for nextIdx in range(wordLen):
            if (curIdx == nextIdx):
                continue;
                
            if (isVisited[nextIdx]):
                continue;
                
            if (not isConnected[curIdx][nextIdx]):
                continue;
                
            dq.appendleft([nextIdx, curCnt + 1]);
            
    return 0;

def solution(begin, target, words):
    words.insert(0, begin);
    # words.append(target);
    
    wordLen = len(words);
    
    """
    isVisited = [False for word in range(wordLen)];
    isConnected = [[False for col in range(wordLen)] for row in range(wordLen)];
    """
    
    for row in range(wordLen):
        tmpList = []
        isVisited.append(False);
        
        for col in range(wordLen):
            tmpList.append(False);
            
        isConnected.append(tmpList);
    
    makeConnect(words, wordLen);
    
    # print(words);
    # print(isVisited);
    # print(isConnected);
    
    answer = bfs(begin, target, words, wordLen);
    
    return answer;
