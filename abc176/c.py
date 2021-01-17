# ✅
from sys import stdin

def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    max_h = 0
    ans = 0
    for h in a:
        if max_h <= h:
            max_h = h
        else:
            ans += max_h - h
    print(ans)
if __name__=='__main__':
    main()