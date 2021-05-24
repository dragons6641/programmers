def solution(citations):
    answer = -1;
    citationLen = len(citations)
    
    citations.sort(reverse = True);
    
    for i in range(citationLen):
        if (citations[i] == 0):
            answer = i;
            break;
        elif (citations[i] == i + 1):
            answer = i + 1;
            break;
        elif (citations[i] < i + 1):
            answer = i;
            break;
    
    # print(citations);
    
    if (answer == -1):
        answer = citationLen;
    
    return answer;
