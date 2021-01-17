# 途中
from sys import stdin
import itertools

def main():
    input = stdin.readline
    x, k, d = map(int, input().split())
    x = abs(x)
    m = min(k, x/d)
    k -= m
    x -= m*d
    if k % 2 == 0:
        ans = x
    else:
        ans = d - x
    print(int(ans))

if __name__=='__main__':
    main()