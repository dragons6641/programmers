# 참고 코드 : https://velog.io/@rapsby/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%97%AC%ED%96%89%EA%B2%BD%EB%A1%9C-python

beginAirport = 'ICN';

def solution(tickets):
    # 여러 개의 경로 중에서 알파벳 순서가 앞서는 경로 하나만 찾으면 문제를 해결할 수 있다.
    answer = [];
    # 항공권의 리스트에서 알파벳순으로 원소를 추출하기 위해서 역순 정렬하여 스택으로 사용한다.
    s = [beginAirport];
    # dictionary에 공항을 key 값으로 하며, 갈 수 있는 항공권의 리스트를 value 값으로 한다.
    connectDict = {};
    
    # 1. tickets을 순회하여 dictionary를 구성한다.
    for ticket in tickets:
        (src, dst) = ticket;
        connectDict[src] = connectDict.get(src, []) + [dst];
        
    # print(connectDict);
        
    # 2. dictionary를 순회하여 항공권의 리스트를 역순으로 정렬한다.
    for connect in connectDict:
        connectDict[connect].sort(reverse = True);
        
    # print(connectDict);
        
    while (len(s) > 0):
        top = s[-1];

        # print(answer);
        # print(s);
        # print(top);
        # print();
        
        # 3. 인천을 시작으로 갈 수 있는 항공권이 있으면 항공권의 리스트에서 추출하고 별도의 스택에 저장한다.
        if top in connectDict and connectDict[top]:
            s.append(connectDict[top].pop());
        # 4. 갈 수 있는 항공권이 없으면 스택에서 추출하여 경로에 추가한다.
        else:
            answer.append(s.pop());
            
    # print(answer);
    
    # 5. 경로에서는 스택에서 pop한 내용이 역순으로 저장되므로 경로의 역순을 반환한다.
    answer.reverse();
    
    # print(answer);
    
    return answer;
