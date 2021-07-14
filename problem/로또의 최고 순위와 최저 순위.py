MAX_NUM = 45;
LOTTO_TUPLE = (6, 6, 5, 4, 3, 2, 1);

def solution(lottos, win_nums):
    winCnt = [0, 0];
    winNumList = [False for _ in range(MAX_NUM + 1)];
    
    for curWinNum in win_nums:
        winNumList[curWinNum] = True;
        
    for curLotto in lottos:
        if (curLotto == 0):
            winCnt[0] += 1;
        elif (winNumList[curLotto]):
            (winCnt[0], winCnt[1]) = (winCnt[0] + 1, winCnt[1] + 1);
    
    return [LOTTO_TUPLE[winCnt[0]], LOTTO_TUPLE[winCnt[1]]];
