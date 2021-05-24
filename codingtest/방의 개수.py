# 어렵다... 그냥 내 능력으로는 풀 수가 없다...
# 일단은 참고 코드 그대로 작성하고 이해라도 해보자
# 참고 코드 : https://pf333.tistory.com/86

import collections;

startRow = 0;
startCol = 0;
moveDist = 2;

def solution(arrows):
    answer = 0;
    dirList = [(-1, 0), (-1, 1), (0, 1),  (1, 1), \
              (1, 0), (1, -1), (0, -1), (-1, -1)];
    curPos = (startRow, startCol);
    
    # vertexVisited : 노드 방문 체크
    vertexVisited = collections.defaultdict(bool);
    
    # edgeVisited : 노드 방문 경로 체크 ((src, dst)는 src -> dst 경로를 의미)
    edgeVisited = collections.defaultdict(bool);
    
    # arrows 따라 노드 좌표를 큐에 추가
    dq = collections.deque([curPos]);
    
    # print(dirList);
    # print(vertexVisited);
    # print(edgeVisited);
    # print(dq);
    
    for r in arrows:
        # 모래 시계 형태 예외를 처리하기 위해 해당 방향으로 2칸씩 추가한다. 
        for k in range(moveDist):
            nextPos = (curPos[0] + dirList[r][0], curPos[1] + dirList[r][1]);
            
            dq.append(nextPos);
            
            curPos = nextPos;
            
    curPos = dq.popleft();
    
    vertexVisited[curPos] = True;
    
    while (dq):
        nextPos = dq.popleft();
        
        # 이미 방문한 노드(vertexVisited[node] == True)인 경우
        if (vertexVisited[nextPos]):
            # 해당 경로로 처음 들어온 경우 answer += 1
            # 처음 들어온 경우에 방이 처음 생성되므로!
            if (not edgeVisited[(curPos, nextPos)]):
                answer += 1;
        # 처음 방문한 노드인 경우 방문 체크를 한다.
        else:
            vertexVisited[nextPos] = True;
            
        # 해당 노드로 들어온 경로를 방문 체크해준다. 
        edgeVisited[(curPos, nextPos)] = True;
        edgeVisited[(nextPos, curPos)] = True;
        curPos = nextPos;
    
    return answer;
