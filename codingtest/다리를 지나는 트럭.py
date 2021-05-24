import collections;

def solution(bridge_length, weight, truck_weights):
    answer = 0;
    curWeight = 0;
    truckIdx = 0;
    truckCnt = len(truck_weights);
    dq = collections.deque();
    
    while ((len(dq) > 0) or (truckIdx < truckCnt)):
        # print("answer =", answer);
        # print("curWeight =", curWeight);
        # print("truckIdx =", truckIdx);
        # print(dq);
        # print();
        
        answer += 1;
        
        if (len(dq) > 0):
            (firstTime, firstWeight) = dq[0];
            
            # print(firstTime, firstWeight);
            
            if (answer - firstTime == bridge_length):
                # print("pop!");
                
                dq.popleft();
                curWeight -= firstWeight;
        
        if (truckIdx < truckCnt):
            nextWeight = truck_weights[truckIdx];
            
            # print("nextWeight =", nextWeight);
        
            if (curWeight + nextWeight <= weight):
                # print("push!");

                dq.append([answer, nextWeight]);
                curWeight += nextWeight;
                truckIdx += 1;
    
    return answer;
