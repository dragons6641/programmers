# 참고 코드 : https://johnyejin.tistory.com/132

def solution(jobs):
    answer = 0;
    curTime = 0;
    jobCnt = len(jobs);
    
    # 1. jobs 배열은 소요시간을 기준으로 오름차순 정렬을 한다. 
    # 소요시간이 작을수록 각 작업들이 기다리는 시간이 줄어들기 때문이다.
    jobs.sort(key = lambda k : k[1]);
    
    # print(jobs);
    
    # 2. jobs 배열이 empty가 될때까지 while문을 돌린다.
    while (jobs):
        # 3. jobs 길이만큼 for문을 돌리면서 해당 작업의 요청시간이 start(현재까지 진행된 작업 시간)보다 작으면, 
        for jobIdx in range(len(jobs)):
            (nextRequest, nextDuration) = jobs[jobIdx];
            
            # print(nextRequest, nextDuration);
            
            # 즉, 해당 작업이 진행된 시간보다 먼저 요청이 들어왔으면,
            if (curTime >= nextRequest):
                # 해당 작업을 진행시키고 jobs 배열에서 지워버린다.
                curTime += nextDuration;
                answer += (curTime - nextRequest);
                jobs.pop(jobIdx);
                
                # print(curTime, answer);
                
                break;
                
            if (jobIdx == len(jobs) - 1):
                curTime += 1;
    
    answer //= jobCnt;
    
    return answer;
