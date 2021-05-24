import math;

def calcDivisor(brown, yellow):
    area = brown + yellow;
    maxLoop = math.ceil(math.sqrt(area));
    
    for height in range(3, maxLoop + 1):
        if (area % height == 0):
            width = int(area / height);
            
            if ((width - 2) * (height - 2) == yellow):
                return [width, height];
        
    return [];

def solution(brown, yellow):
    answer = calcDivisor(brown, yellow);
    
    return answer;
