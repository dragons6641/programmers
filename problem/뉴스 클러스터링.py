# 뉴스 클러스터링

from datetime import datetime;

def solution(str1, str2):
    answer = 0;

    # 교집합 원소 갯수
    ci = 0;

    # 합집합 원소 갯수
    cu = 0;

    # multi-set
    ms1 = [];
    ms2 = [];

    # 다중집합1 만들기
    for i in range(len(str1) - 1):
        # 문자만 해당한다!
        # 대문자 소문자 모두!
        # 첫 번째 글자
        if (((str1[i] >= 'A') and (str1[i] <= 'Z')) or ((str1[i] >= 'a') and (str1[i] <= 'z'))):
            # 두 번째 글자
            if (((str1[i + 1] >= 'A') and (str1[i + 1] <= 'Z')) or ((str1[i + 1] >= 'a') and (str1[i + 1] <= 'z'))):
                # 부분집합 인정
                ms1.append(str1[i].lower() + str1[i + 1].lower());

    # 다중집합2 만들기
    for i in range(len(str2) - 1):
        # 문자만 해당한다!
        # 대문자 소문자 모두!
        # 첫 번째 글자
        if (((str2[i] >= 'A') and (str2[i] <= 'Z')) or ((str2[i] >= 'a') and (str2[i] <= 'z'))):
            # 두 번째 글자
            if (((str2[i + 1] >= 'A') and (str2[i + 1] <= 'Z')) or ((str2[i + 1] >= 'a') and (str2[i + 1] <= 'z'))):
                # 부분집합 인정
                ms2.append(str2[i].lower() + str2[i + 1].lower());

    # 전체 경우의 수 만들기
    s1 = set(ms1);
    s2 = set(ms2);

    # 합집합
    us = s1 | s2;

    # 전체 경우의 수에서 교집합, 합집합 구하기
    for i in us:
        # 몇 개 들어있는지 센다
        c1 = ms1.count(i);
        c2 = ms2.count(i);

        # 교집합은 최솟값
        ci += min([c1, c2]);

        # 합집합은 최댓값
        cu += max([c1, c2]);

    # 0으로 나눌 경우
    if (cu == 0):
        answer = 65536

    # 일반적인 경우
    else:
        answer = (int)((ci * 65536) / cu);

    return answer;

"""
str1 = "handshake";
str2 = "shake hands";

# multi-set
ms1 = [];
ms2 = [];

# 다중집합1 만들기
for i in range(len(str1) - 1):
    # 문자만 해당한다!
    # 대문자 소문자 모두!
    # 첫 번째 글자
    if (((str1[i] >= 'A') and (str1[i] <= 'Z')) or ((str1[i] >= 'a') and (str1[i] <= 'z'))):
        # 두 번째 글자
        if (((str1[i + 1] >= 'A') and (str1[i + 1] <= 'Z')) or ((str1[i + 1] >= 'a') and (str1[i + 1] <= 'z'))):
            # 부분집합 인정
            ms1.append(str1[i].lower() + str1[i + 1].lower());

# 다중집합2 만들기
for i in range(len(str2) - 1):
    # 문자만 해당한다!
    # 대문자 소문자 모두!
    # 첫 번째 글자
    if (((str2[i] >= 'A') and (str2[i] <= 'Z')) or ((str2[i] >= 'a') and (str2[i] <= 'z'))):
        # 두 번째 글자
        if (((str2[i + 1] >= 'A') and (str2[i + 1] <= 'Z')) or ((str2[i + 1] >= 'a') and (str2[i + 1] <= 'z'))):
            # 부분집합 인정
            ms2.append(str2[i].lower() + str2[i + 1].lower());

ms1.sort();
ms2.sort();

print(ms1);
print(ms2);
"""
