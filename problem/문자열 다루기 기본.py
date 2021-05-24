def solution(s):
    if (len(s) == 4 or len(s) == 6):
        for i in s:
            if i >= '0' and i <= '9':
                continue;
            else:
                return False;
    else:
        return False;
    return True;
