# 추석 트래픽

from datetime import datetime;
from datetime import timedelta;

def solution(lines):
    answer = 0;
    cnt = 0;
    timelist = [];
    
    # print(lines);
    
    for i in lines:
        S = datetime.strptime(i.split(' ')[1], '%H:%M:%S.%f');
        # print(S);
        
        endTime = datetime(2016, 9, 15, 0, 0, 0, 0);
        endTime += timedelta(hours = S.hour, minutes = S.minute, 
                            seconds = S.second, microseconds = S.microsecond)
        # print(S.hour, S.minute, S.second, S.microsecond);
        # print(endTime);
        
        T = float(i.split(' ')[2][0:-1]);
        # print(T);
        
        startTime = endTime;
        endTime += timedelta(seconds = 0.999)
        startTime -= timedelta(seconds = T - 0.001);
        # print(startTime);
        
        timelist.append([startTime, -1])
        timelist.append([endTime, 1]);
        
    timelist = sorted(timelist, key = lambda x : (x[0], x[1]));
    # print(timelist);
    
    for i in timelist:
        if (i[1] == -1):
            cnt += 1;
            
            if (answer < cnt):
                answer = cnt;
        elif (i[1] == 1):
            cnt -= 1;
            
        # print(i, cnt);
    
    return answer;

"""
from datetime import datetime;
from datetime import timedelta;

def solution(lines):
    answer = 0;

    # 시작 시간만 따로 저장할 배열
    starts = [];

    # 끝 시간만 따로 저장할 배열
    ends = [];

    for i in range(len(lines)):
        tmp = datetime(2016, 9, 15, 0, 0, 0, 0);

        # 공백 기준으로 분리
        lines[i] = lines[i].split();

        tmp = datetime.strptime(lines[i][1], "%H:%M:%S.%f");
        # tmp.microsecond /= 100;
        ends.append(tmp);

        # 소수점 없을 경우
        if (len(lines[i][2]) == 2):
            tmp = datetime.strptime(lines[i][2], "%Ss");

        # 소수점 있을 경우
        else:
            tmp = datetime.strptime(lines[i][2], "%S.%fs");

        d = timedelta(seconds = tmp.second, microseconds = tmp.microsecond - 1000);
        starts.append(ends[-1] - d);

    # 전체 트래픽 시작 시간
    s = starts[0];

    # 전체 트래픽 끝 시간
    e = ends[-1];

    # 최소 단위
    d = timedelta(microseconds = 1000)

    # 구간 시작
    cur_s = s;
    cur_e = s + d;

    # 시작 인덱스
    si = 0;

    # 끝 인덱스
    ei = 0;

    # 시작부터 끝까지
    while (True):
        for i in range(si, len(starts)):
            # 시작 시간이 현재 구간에 포함이면
            if ((starts[si] >= cur_s) and (starts[si] <= cur_e)):
                # 다음 것 확인
                si += 1;

            # 포함되지 않으면
            else:
                break;

        for i in range(ei, len(ends)):
            # 끝 시간이 현재 구간에 포함이면
            if ((ends[ei] >= cur_s) and (ends[ei] <= cur_e)):
                # 다음 것 확인
                ei += 1;

            # 포함되지 않으면
            else:
                break;

        if ((ei - si) > answer):
            answer = ei - si;

        # 마지막에는 다음 구간으로
        cur_s += d;
        cur_e += d;

        # 구간을 초과하면
        if (cur_e > e):
            # 모두 확인했으니 종료
            break;

    return answer;
"""
    

"""
lines = [
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]

# 시작 시간만 따로 저장할 배열
starts = [];

# 끝 시간만 따로 저장할 배열
ends = [];


for i in range(len(lines)):
    tmp = datetime(2016, 9, 15, 0, 0, 0, 0);

    # 공백 기준으로 분리
    lines[i] = lines[i].split();

    tmp = datetime.strptime(lines[i][1], "%H:%M:%S.%f");
    # tmp.microsecond /= 100;
    ends.append(tmp);

    # 소수점 없을 경우
    if (len(lines[i][2]) == 2):
        tmp = datetime.strptime(lines[i][2], "%Ss");

    # 소수점 있을 경우
    else:
        tmp = datetime.strptime(lines[i][2], "%S.%fs");

    d = timedelta(seconds = tmp.second, microseconds = tmp.microsecond - 1000);
    starts.append(ends[-1] - d);

# print(lines);
print(starts);
print(ends);
"""
