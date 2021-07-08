MAX_DIGIT = 5;

def solution(files):
    answer = [];
    
    for fileIdx in range(len(files)):
        (startIdx, endIdx, tmpList) = (0, 0, []);
        
        while (not files[fileIdx][endIdx].isdigit()):
            endIdx += 1;
        
        tmpList.extend([fileIdx, files[fileIdx][startIdx : endIdx]]);
        startIdx = endIdx;
        
        while (endIdx < len(files[fileIdx]) and 
               (endIdx - startIdx < MAX_DIGIT) and 
               files[fileIdx][endIdx].isdigit()):
            endIdx += 1;
            
        tmpList.extend([files[fileIdx][startIdx : endIdx], 
                        ('' if endIdx == len(files[fileIdx]) else files[fileIdx][endIdx : ])]);
        answer.append(tmpList);
        
        # print(curFile);
        # print(tmpList);
    
    answer.sort(key = lambda k : (k[1].lower(), int(k[2]), k[0]));

    for curIdx in range(len(answer)):
        answer[curIdx] = ''.join(answer[curIdx][1 : ]);
        
    # print(answer);
    
    return answer;
