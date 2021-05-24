import math;

digit = 10;
# isVisited = [];
isPrime = [];
cntList = [0 for i in range(digit)];
ansSet = set();

def checkPrime(maxNum):
    maxLoop = math.ceil(math.sqrt(maxNum));
    
    for num in range(2):
        isPrime.append(False);
    
    for num in range(2, maxNum):
        isPrime.append(True);
        
    for divisor in range(2, maxLoop + 1):
        # print(divisor);
        
        for k in range(divisor * 2, maxNum, divisor):
            # print(k);
            
            isPrime[k] = False;

def backtrack(numbers, numLen, depth, result):
    """
    if (depth == numLen):
        print(result);
        
        ansSet.add(int(result));

    for numIdx in range(numLen):
        if (not isVisited[numIdx]):
            isVisited[numIdx] = True;
            
            backtrack(numbers, numLen, depth + 1, result + numbers[numIdx]);
            
            isVisited[numIdx] = False;
    """
    
    if (isPrime[result]):
            ansSet.add(int(result));
    
    if (depth == numLen):
        # print(result);
        
        return;
    
    for k in range(digit):
        if (cntList[k] > 0):
            cntList[k] -= 1;

            backtrack(numbers, numLen, depth + 1, (result * digit) + k);
            
            cntList[k] += 1;

def solution(numbers):
    answer = 0;
    numLen = len(numbers);
    maxNum = 10 ** numLen;
    
    checkPrime(maxNum);
    
    """
    for number in numbers:
        isVisited.append(False);
    """
    
    for number in numbers:
        cntList[int(number)] += 1;
    
    # print(isVisited);
    # print(isPrime);
    # print(cntList);
    
    # backtrack(numbers, numLen, 0, '')
    backtrack(numbers, numLen, 0, 0)
    
    answer = len(ansSet);
    
    # print(ansSet);
    
    return answer;
