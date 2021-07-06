START_CHR = ord("A");
ALPHABET_CNT = 26;
WORD_DICT = dict(zip([chr(k) for k in range(START_CHR, START_CHR + ALPHABET_CNT)], 
                     [k for k in range(1, ALPHABET_CNT + 1)]));

def solution(msg):
    answer = [];
    (wordCnt, startIdx) = (ALPHABET_CNT, 0);
    
    while (startIdx < len(msg)):
        endIdx = startIdx + 1;
        
        while (endIdx < len(msg)):
            if (msg[startIdx : endIdx] in WORD_DICT.keys()):
                endIdx += 1;
                continue;
            else:
                answer.append(WORD_DICT[msg[startIdx : endIdx - 1]]);
                wordCnt += 1;
                WORD_DICT[msg[startIdx : endIdx]] = wordCnt;
                break;
        
        # print(startIdx, endIdx, msg[startIdx : endIdx]);
        
        if (endIdx == len(msg)):
            if (msg[startIdx : endIdx] in WORD_DICT.keys()):
                answer.append(WORD_DICT[msg[startIdx : ]]);
                endIdx += 1;
            else:
                answer.append(WORD_DICT[msg[startIdx : endIdx - 1]]);
                wordCnt += 1;
                WORD_DICT[msg[startIdx : endIdx]] = wordCnt;
        
        startIdx = endIdx - 1;
            
    # print(WORD_DICT);
    
    return answer;
