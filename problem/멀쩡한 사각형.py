import math;

def solution(w, h):
    gcd = math.gcd(w, h);
    (c, r) = (w // gcd, h // gcd);
    
    return ((w * h) - (gcd * (c + r - 1)));
