# maxNumber = 32000;
maxDepth = 8;

def solution(N, number):
    answer = -1;
    
    """
    dp = [0 for i in range(maxNumber + 1)];
    
    print(len(dp));
    """
    
    if (N == number):
        return 1;
    
    dpList = [{}, {N}];
    
    for curDepth in range(2, maxDepth + 1):
        tmpSet = {int(str(N) * curDepth)};
        
        for halfDepth in range(1, (curDepth // 2) + 1):
            # print(curDepth, halfDepth, curDepth - halfDepth);
            
            for firstElement in dpList[halfDepth]:
                for secondElement in dpList[curDepth - halfDepth]:
                    # print(firstElement, secondElement)
                    
                    tmpSet.add(firstElement + secondElement);
                    tmpSet.add(firstElement * secondElement);
                    tmpSet.add(firstElement - secondElement);
                    tmpSet.add(secondElement - firstElement);
                    
                    if (secondElement != 0):
                        tmpSet.add(firstElement // secondElement);
                        
                    if (firstElement != 0):
                        tmpSet.add(secondElement // firstElement);
        
        # print(tmpSet);
        
        if number in tmpSet:
            return curDepth;
        
        dpList.append(tmpSet);
        
        # print(dpList);
    
    # print(dpList);
    
    return answer;
