def makeTrie(wordList):
    root = {};
    
    for word in wordList:
        cur = root;
        
        for ch in word:
            if '\0' in cur:
                return False;
            
            cur = cur.setdefault(ch, {});
        
        cur['\0'] = '\0';
        
        print(root);
    
    return True;

def solution(phone_book):
    phone_book.sort(key = lambda k : len(k));
    
    # print(phone_book);
    
    answer = makeTrie(phone_book);
    
    return answer;
