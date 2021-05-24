def solution(n, lost, reserve):
    lostSet = set(lost);
    reserveSet = set(reserve);
    
    lost = sorted(list(lostSet - reserveSet));
    reserve = sorted(list(reserveSet - lostSet));
    
    lostCnt = len(lost);
    reserveCnt = len(reserve);
    answer = n - lostCnt;
    lostIdx = 0;
    reserveIdx = 0;
    
    while ((lostIdx < lostCnt) and (reserveIdx < reserveCnt)):
        curLost = lost[lostIdx];
        curReserve = reserve[reserveIdx];
        
        if (curLost < curReserve):
            if (curLost + 1 == curReserve):
                answer += 1;
                lostIdx += 1;
                reserveIdx += 1;
            else:
                lostIdx += 1;
        elif (curLost > curReserve):
            if (curLost == curReserve + 1):
                answer += 1;
                lostIdx += 1;
                reserveIdx += 1;
            else:
                reserveIdx += 1;
        else:
            answer += 1;
            lostIdx += 1;
            reserveIdx += 1;
    
    return answer;
