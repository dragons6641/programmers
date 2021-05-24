dpq = [];

def pushNum(num):
    dpq.append(num);
    
    return;

def popMax():
    if (len(dpq) > 0):
        dpq.remove(max(dpq));
    
    return;

def popMin():
    if (len(dpq) > 0):
        dpq.remove(min(dpq));
    
    return;

def solution(operations):
    answer = [0, 0];
    
    for operation in operations:
        (cmd, num) = operation.split(' ');
        
        num = int(num);
        
        print(cmd, num);
        
        if (cmd == 'I'):
            pushNum(num);
        elif (num == 1):
            popMax();
        elif (num == -1):
            popMin();
    
    if (len(dpq) > 0):
        answer = [max(dpq), min(dpq)];
    
    return answer;
