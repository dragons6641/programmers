import collections;

def solution(priorities, location):
    answer = 0;
    ansList = [];
    priorityCnt = len(priorities);
    pc = collections.Counter(priorities);
    dq = collections.deque(enumerate(priorities));
    
    # print(pc);
    # print(dq);
    
    while (len(dq) > 0):
        flag = True;
        
        (firstIdx, firstPriority) = dq.popleft();
        pc[firstPriority] -= 1;
        
        # print(firstIdx, firstPriority);
        
        for key in pc.keys():
            if ((key > firstPriority) and (pc[key] > 0)):
                # print("push!");
                
                flag = False;
                
                dq.append((firstIdx, firstPriority));
                pc[firstPriority] += 1;
                
                break;
        
        if (flag):
            ansList.append(firstIdx);
    
    # print(ansList);
    
    answer = ansList.index(location) + 1;
    
    return answer;
