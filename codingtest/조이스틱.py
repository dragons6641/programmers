import collections;

startOrd = ord('A');
halfOrd = ord('O');
endOrd = ord('Z');
maxNameLen = 20;

def solution(name):
    answer = 0;
    cursor = 0;
    nameLen = len(name);
    dq = collections.deque();
    
    for nameIdx in range(nameLen):
        curOrd = ord(name[nameIdx]);
        
        if (curOrd == startOrd):
            continue;
        
        if (curOrd < halfOrd):
            dq.append([nameIdx, (curOrd - startOrd)]);
        else:
            dq.append([nameIdx, (endOrd - curOrd + 1)]);
            
    # print(dq);
    
    while (dq):
        dqLen = len(dq);
        
        if (dqLen == 0):
            break;
        
        leftIdx = dq[0][0];
        rightIdx = dq[-1][0];
        
        if (leftIdx >= cursor):
            leftMove = leftIdx - cursor;
        else:
            leftMove = leftIdx + nameLen - cursor;
        
        if (rightIdx <= cursor):
            rightMove = cursor - rightIdx;
        else:
            rightMove = cursor + nameLen - rightIdx;
        
        # print(dq);
        # print("cursor =", cursor);
        # print("idx =", leftIdx, rightIdx);
        # print("move =", leftMove, rightMove);
        
        if (leftMove <= rightMove):
            answer += (leftMove + dq[0][1]);
            cursor = leftIdx;
            dq.popleft();
        else:
            answer += (rightMove + dq[-1][1]);
            cursor = rightIdx;
            dq.pop();
            
        # print("answer =", answer);
        # print();
    
    return answer;
