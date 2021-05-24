import heapq;

def solution(scoville, K):
    answer = 0;
    
    heapq.heapify(scoville);
    
    while (len(scoville) > 1) and (scoville[0] < K):
        nextScoville = 0;
        
        for i in range(1, 3):
            nextScoville += scoville[0] * i;
            heapq.heappop(scoville);
            
        answer += 1;
        heapq.heappush(scoville, nextScoville);
        
        # print(nextScoville);
        # print(scoville);
        
    if (scoville[0] < K):
        answer = -1;
    
    return answer;
