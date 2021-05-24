# 다트 게임

def solution(dartResult):
    answer = 0;

    score = [];

    # 한 글자씩 읽어야 한다
    for i in range(len(dartResult)):
        cur = dartResult[i];

        # print(cur, end=' ');

        # 점수
        if (cur >= '2' and cur <= '9'):
            score.append((int)(cur));
            
        # 0과 10 구분
        elif (cur == '0'):
            # 처음이면
            if (i == 0):
                # 무조건 0
                score.append(0);
            # 처음 아니면
            else:
                # 그 이전이 1이면
                if (dartResult[i - 1] == '1'):
                    # 10점이다
                    score.append(10);
                # 나머지는
                else:
                    # 0점이다
                    score.append(0);

        # 0과 10 구분
        elif (cur == '1'):
            # 그 다음이 0이 아닐 경우에는
            if (dartResult[i + 1] != '0'):
                score.append(1);

        # 보너스
        # 싱글
        elif (cur == 'S'):
            score[-1] **= 1;

        # 더블
        elif (cur == 'D'):
            score[-1] **= 2;

        # 트리플
        elif (cur == 'T'):
            score[-1] **= 3;

        # 옵션
        # 스타상
        elif (cur == '*'):
            # 처음 나왔을 경우
            if (len(score) == 1):
                score[-1] *= 2;

            # 이외의 경우
            else:
                score[-1] *= 2;
                score[-2] *= 2;

        # 아차상
        elif (cur == '#'):
            score[-1] *= -1;

        # print(score);

    # 최종 점수
    for i in score:
        answer += i;

    return answer;

"""
dartResult = "1D2S#10S";

answer = solution(dartResult);

print(answer);
"""
