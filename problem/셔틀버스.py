# 셔틀버스

from datetime import datetime;
from datetime import timedelta;

def solution(n, t, m, timetable):
    answer = '';

    # 일단 정렬
    timetable.sort();

    # 다음 크루
    index = 0;

    # 전체 셔틀버스 TO
    total = n * m;

    # 첫 셔틀버스 출발 시각
    first = datetime(1900, 1, 1, 9, 0);

    # 답안 시간
    ans_time = first;
    
    # 현재 시각
    cur = first;

    # 셔틀버스 운행 간격
    d = timedelta(minutes = t);

    # 셔틀버스 시간 만들기
    shuttle = [];

    # 시간 변환
    for i in range(len(timetable)):
        # 24:00은 예외처리
        if (timetable[i] == "24:00"):
            timetable[i] = datetime(1900, 1, 2, 0, 0);
        # 일반적인 경우
        else:
            timetable[i] = datetime.strptime(timetable[i], "%H:%M");

    # 셔틀 운행 횟수만큼 반복
    for i in range(n):
        # 셔틀버스 시간으로 추가
        shuttle.append(cur);

        # 다음 셔틀버스 출발시각 구하기
        cur += d;

    # 셔틀 시간이 기준!
    for i in shuttle:
        # 이번 셔틀에 타고 가는 사람 수
        cnt = 0;

        # 아직 탈 사람 남은 경우에만
        if (index < len(timetable)):
            # 도착한 크루들은 시간순 정렬
            for j in range(index, len(timetable)):
                # 태울 수 있으면
                if ((i >= timetable[j]) and (cnt < m)):
                    # 한 명 태웠다
                    cnt += 1;
                # 태울 수 없으면
                else:
                    break;

            # 태우고 간 사람만큼 index 증가
            index += cnt;

            # 한 번 태웠을 때마다 확인
            # 자리가 남는다면
            if (cnt < m):
                # 콘 태우고 갈 수 있다
                # 셔틀 오는 시간에 딱 맞춰서 오면 됨
                ans_time = i;
            # 자리 안남는다면
            else:
                # 이번 셔틀 억지로라도 타야지
                # 마지막 탄 사람보다 1분 빨리 오면 탈 수 있다!
                d = timedelta(minutes = 1);

                # 그런데 아직 아무도 안 태웠다면
                if (index == 0):
                    ans_time = timetable[index] - d;
                # 누군가 타긴 했다면
                elif (index <= len(timetable)):
                    ans_time = timetable[index - 1] - d;

    # 시간을 문자열으로 변환
    answer = ans_time.strftime("%H:%M");

    return answer;

"""
n = 10;
t = 60;
timetable = ["08:00", "08:01", "08:02", "08:03"]

# 첫 셔틀버스 출발 시각
first = datetime(1900, 1, 1, 9, 0);

# 현재 시각
cur = first;

# 셔틀버스 운행 간격
d = timedelta(minutes = t);

# 셔틀버스 시간 만들기
shuttle = [];

# 시간 변환
for i in range(len(timetable)):
    timetable[i] = datetime.strptime(timetable[i], "%H:%M");

# 셔틀 운행 횟수만큼 반복
for i in range(n):
    # 셔틀버스 시간으로 추가
    shuttle.append(cur);

    # 다음 셔틀버스 출발시각 구하기
    cur += d;

print(shuttle);
print(timetable);
"""
