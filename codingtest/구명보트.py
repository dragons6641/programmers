maxAboard = 2;

def solution(people, limit):
    answer = 0;
    peopleCnt = len(people);
    boatWeight = 0;
    leftIdx = 0;
    rightIdx = peopleCnt - 1;
    
    people.sort();
    
    # print(people);
    
    """
    for curWeight in people:
        nextWeight = boatWeight + curWeight;
        
        if ((nextWeight > limit) or (aboardCnt == maxAboard)):
            nextWeight = curWeight;
            aboardCnt = 1;
            answer += 1;
        else:
            boatWeight = nextWeight;
            aboardCnt += 1;
            
    if (aboardCnt > 0):
        answer += 1;
    """
    
    while (leftIdx <= rightIdx):
        leftWeight = people[leftIdx];
        rightWeight = people[rightIdx];
        sumWeight = leftWeight + rightWeight;
        
        # print("idx =", leftIdx, rightIdx);
        # print("weight =", leftWeight, rightWeight);
        # print("sum =", sumWeight);
        # print("limit =", limit);
        
        if (sumWeight > limit):
            rightIdx -= 1;
            answer += 1;
        else:
            leftIdx += 1;
            rightIdx -= 1;
            answer += 1;
                
        # print("answer =", answer);
        # print();
    
    return answer;
