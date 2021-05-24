# 캐시

def solution(cacheSize, cities):
    answer = 0;
    cur_city = '';

    cache = [];

    # 도시 하나씩 읽으면서
    for i in range(len(cities)):
        # 소문자로 변환
        cur_city = cities[i].lower();

        # 캐시에 있으면
        if (cur_city in cache):
            # hit
            # 이미 있는 것 지우고
            cache.remove(cur_city);

            # 뒤에 새로 넣는다!
            cache.append(cur_city);

            # 시간은 1초
            answer += 1;

        # 캐시에 없으면
        else:
            # 공간 충분하면
            if (len(cache) < cacheSize):
                # 뒤에 새로 넣는다!
                cache.append(cur_city);

            # 공간 없으면
            else:
                # 캐시 크기가 0 이상일 경우에만
                if (cacheSize > 0):
                    # 가장 앞에 있는 것 지우고
                    del(cache[0]);

                    # 뒤에 새로 넣는다!
                    cache.append(cur_city);

            # 시간은 5초
            answer += 5;

    return answer;
