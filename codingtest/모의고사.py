def solution(answers):
    answer = [];
    guessList = [];
    lenList = [];
    cntList = [0, 0, 0];
    
    guessList.append([1, 2, 3, 4, 5]);
    guessList.append([2, 1, 2, 3, 2, 4, 2, 5]);
    guessList.append([3, 3, 1, 1, 2, 2, 4, 4, 5, 5]);
    
    for guess in guessList:
        lenList.append(len(guess));
    
    # print(guessList);
    # print(lenList);
    
    for ansIdx in range(len(answers)):
        for guessIdx in range(len(guessList)):
            if (guessList[guessIdx][ansIdx % lenList[guessIdx]] == answers[ansIdx]):
                cntList[guessIdx] += 1;
                
    # print(cntList);
    
    maxVal = max(cntList);
    
    for cntIdx in range(len(cntList)):
        if (cntList[cntIdx] == maxVal):
            answer.append(cntIdx + 1);
    
    return answer;
