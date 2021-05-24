# 비밀지도

def solution(n, arr1, arr2):
    answer = [];

    # 변환
    for i in range(n):
        # 2진수 문자열로 바꾸고
        # 접두어 제거한 뒤
        n1 = format(arr1[i], 'b');
        n2 = format(arr2[i], 'b');

        """
        # 자릿수 맞춰줘야 한다!
        if (len(n1) < n):
            for i in range(n - len(n1)):
                n1.insert(0, '0');

        if (len(n2) < n):
            for i in range(n - len(n2)):
                n2.insert(0, '0');
        """

        # 자릿수 맞춰줘야 한다!
        # 그 문자열로 치환
        arr1[i] = n1.zfill(n);
        arr2[i] = n2.zfill(n);

    # 출력
    for row in range(n):
        # 한 줄은 여기에 만들자
        tmp = '';

        for col in range(n):
            # 문자 하나씩 비교
            cur1 = arr1[row][col];
            cur2 = arr2[row][col];

            # 하나라도 벽이면
            if (cur1 == '1' or cur2 == '1'):
                # 전체 지도에서도 벽
                # print('#', end = '');
                tmp += '#';

            # 모두 공백이면
            else:
                # 전체 지도에서도 공백
                # print(' ', end = '');
                tmp += ' ';

        # 다음 줄로
        # print();

        answer.append(tmp);

    print(answer);
            
    return answer;
