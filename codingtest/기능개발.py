import math;

maxProgress = 100;

def solution(progresses, speeds):
    answer = [];
    s = [];
    distributeCnt = 0;
    workCnt = len(progresses);
    
    for workIdx in range(workCnt):
        workDay = math.ceil((maxProgress - progresses[workIdx]) / speeds[workIdx]);
        
        # print(workDay);
        
        if (len(s) == 0):
            s.append(workDay);
            distributeCnt = 1;
            continue;
            
        lastDay = s[-1];
        
        if (lastDay < workDay):
            answer.append(distributeCnt);
            
            s.append(workDay);
            distributeCnt = 1;
        else:
            distributeCnt += 1;
    
    answer.append(distributeCnt);
    
    # print(s);
    
    return answer;
