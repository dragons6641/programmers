def compNumber(n):
    mulCnt = int(12 / len(n));
    
    return (n * mulCnt);
        

def solution(numbers):
    answer = '';
    flag = True;
    
    strings = sorted(list(map(str, numbers)), key = compNumber, reverse = True);
    
    # print(numbers);
    
    for string in strings:
        answer += string;
    
    for char in answer:
        if (char != '0'):
            flag = False;
            break;
            
    if (flag):
        answer = '0';
    
    return answer;
