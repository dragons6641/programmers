import itertools;

maxNum = 1000;

def solution(numbers, target):
    answer = 0;
    numLen = len(numbers);
    
    operatorList = ['+', '-'];
    permutationList = list(itertools.product(operatorList, repeat = numLen));
    
    # print(permutationList);
    
    for permutation in permutationList:
        # print(permutation);
        
        result = 0;
        
        for numIdx in range(numLen):  
            if permutation[numIdx] == '+':
                result += numbers[numIdx];
            elif permutation[numIdx] == '-':
                result -= numbers[numIdx];
                
        if (result == target):
            answer += 1;
    
    return answer;
