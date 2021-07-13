import collections;

DIR_CNT = 4;
DIR_VEC = ((-1, 0), (1, 0), (0, -1), (0, 1));

class LandNode:
    def __init__(self, height = 0, r = -1, c = -1) -> None:
        self.parent = self;
        self.rank = 0;
        self.height = height;
        self.r = r;
        self.c = c;
        self.isVisited = False;
        return None;
    
    def printLandNode(self) -> None:
        print(self.parent, self.rank, self.height, self.r, self.c, self.isVisited);
        return None;

def bfs(startNode : LandNode, landArr : list, height : int) -> list:
    edgeList = [];
    startNode.isVisited = True;
    dq = collections.deque([startNode]);
    
    # print('start');
    # print(startNode.r, startNode.c);
    
    while (dq):
        curNode = dq.popleft();
        
        for dirIdx in range(DIR_CNT):
            nextR = curNode.r + DIR_VEC[dirIdx][0];
            nextC = curNode.c + DIR_VEC[dirIdx][1];

            if ((nextR < 0) or (nextR >= len(landArr)) or (nextC < 0) or (nextC >= len(landArr[0]))):
                continue;

            nextNode = landArr[nextR][nextC];

            # print(nextR, nextC, abs(curNode.height - nextNode.height));

            if (nextNode.isVisited):
                continue;
                
            heightDiff = abs(curNode.height - nextNode.height);
                
            if (heightDiff > height):
                edgeList.append([heightDiff, curNode, nextNode]);
                continue;

            # print('next');

            nextNode.parent = startNode;
            nextNode.isVisited = True;
            dq.append(nextNode);
    
    return edgeList;

def find(curNode : LandNode) -> LandNode:
    if (curNode.parent != curNode):
        curNode.parent = find(curNode.parent);
        
    return curNode.parent;

def union(node1 : LandNode, node2 : LandNode) -> None:
    root1 = find(node1);
    root2 = find(node2);
    
    if (root1.rank < root2.rank):
        root1.parent = root2;
    else:
        root2.parent = root1;
        
        if (root1.rank == root2.rank):
            root1.rank += 1;
    
    return None;

def kruskal(edgeList : list) -> int:
    costSum = 0;
    
    for (heightDiff, srcNode, dstNode) in edgeList:
        if (find(srcNode) == find(dstNode)):
            continue;
            
        union(srcNode, dstNode);
        costSum += heightDiff;
    
    return costSum;

def solution(land, height):
    edgeList = [];
    landArr = [[None for c in range(len(land[0]))] for r in range(len(land))];
    
    for r in range(len(land)):
        for c in range(len(land[0])):
            landArr[r][c] = LandNode(land[r][c], r, c);
            
            # landArr[r][c].printLandNode();
            
    for r in range(len(land)):
        for c in range(len(land[0])):
            if (landArr[r][c].isVisited):
                continue;
                
            edgeList.extend(bfs(landArr[r][c], landArr, height));
            
    """
    for r in range(len(land)):
        for c in range(len(land[0])):
            landArr[r][c].parent.printLandNode();
    """
    
    # print(edgeList);
    
    return kruskal(sorted(edgeList, key = lambda k : k[0]));
