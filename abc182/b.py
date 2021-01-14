# ✅
from sys import stdin

def main():
    input = stdin.readline
    n = int(input())
    A = list(map(int, input().split()))

    ans = -1
    mx = 0

    for i in range(2, 1000):
        s = sum(a%i == 0 for a in A)
        if mx < s:
            mx = s
            ans = i
    print(ans)

if __name__=='__main__':
    main()