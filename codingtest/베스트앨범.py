def solution(genres, plays):
    answer = [];
    gDict = {};
    
    for i in range(len(genres)):
        if genres[i] not in gDict.keys():
            gDict[genres[i]] = [[-1, plays[i]], [i, plays[i]]];
        else:
            gDict[genres[i]][0][1] += plays[i];
            gDict[genres[i]].append([i, plays[i]]);
    
    # print(gDict);
    # print(gDict.items())
    
    gList = sorted(gDict.items(), key = lambda k : k[1][0][1], reverse = True)
    
    for i in range(len(gList)):
        gList[i] = list(gList[i]);
        gList[i][1] = sorted(list(gList[i][1]), key = lambda k : k[1], reverse = True);
        
        # print(gList[i]);
        
        for j in range(1, min(len(gList[i][1]), 3)):
            # print(gList[i][1][j]);
            
            answer.append(gList[i][1][j][0])
    
    # print(gList);
    
    return answer;
