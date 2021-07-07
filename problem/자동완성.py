class TrieNode(object):
    def __init__(self, val = ''):
        self.val = val;
        self.cnt = 0;
        self.childDict = dict();
        return None;
    
    def printTrieNode(self):
        print(self.val, self.cnt, self.childDict);
        return None;

def solution(words):
    answer = 0;
    root = TrieNode();
    
    for curWord in words:
        curNode = root;
        
        for curCh in curWord:
            if (curCh in curNode.childDict.keys()):
                curNode = curNode.childDict[curCh];
            else:
                nextNode = TrieNode(curCh);
                curNode.childDict[curCh] = nextNode;
                curNode = nextNode;
            
            curNode.cnt += 1;
            
            # curNode.printTrieNode();
            # print(len(root.childDict), answer);
    
    # root.printTrieNode();
    # print(len(root.childDict));
    
    for curWord in words:
        curNode = root;
        
        for curCh in curWord:
            if (curNode.cnt == 1):
                break;
                
            answer += 1;
            curNode = curNode.childDict[curCh];
            
            # curNode.printTrieNode();
            # print(len(root.childDict), answer);
            
        # print(curWord, answer);
    
    return answer;
