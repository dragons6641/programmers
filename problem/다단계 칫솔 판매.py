SELL_PROFIT = 100;
FEE_RATE = 0.1;

def solution(enroll, referral, seller, amount):
    enrollDict = dict(zip(enroll, map(list, zip(referral, [0 for _ in range(len(enroll))]))));
    enrollDict["-"] = ["-", 0];
    
    # print(enrollDict);
    
    for sellIdx in range(len(seller)):
        curSeller = seller[sellIdx];
        curFee = int(amount[sellIdx] * SELL_PROFIT * FEE_RATE);
        enrollDict[curSeller][1] += amount[sellIdx] * SELL_PROFIT;
        
        # print(curEnroll);
        
        while ((curSeller != "-") and (curFee > 0)):
            # print(curSeller, curFee);
            
            enrollDict[curSeller][1] -= curFee;
            enrollDict[enrollDict[curSeller][0]][1] += curFee;
            curSeller = enrollDict[curSeller][0];
            curFee = int(curFee * FEE_RATE);
            
        # print(enrollDict);
    
    return [enrollDict[k][1] for k in enroll];
