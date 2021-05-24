def solution(participant, completion):
    answer = ''
    pDict = {};
    
    for p in participant:
        if p in pDict.keys():
            pDict[p] += 1;
        else:
            pDict[p] = 1;
    
    # print(pDict);
    
    for c in completion:
        pDict[c] -= 1;
        
    for k in pDict:
        if pDict[k] == 1:
            answer = k;
    
    return answer;
