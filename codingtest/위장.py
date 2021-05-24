def solution(clothes):
    answer = 1;
    cDict = {};
    
    for c in clothes:
        if c[1] in cDict.keys():
            cDict[c[1]] += 1;
        else:
            cDict[c[1]] = 1;
            
    # print(cDict);
    
    for k in cDict:
        answer *= (cDict[k] + 1);
        
    answer -= 1;
    
    return answer;
