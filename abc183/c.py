from sys import stdin
import itertools

def main():
    input = stdin.readline
    n, k = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(n)]
    S = list(itertools.permutations(range(2,n+1)))
    ans = 0
    for s in S:
        s = list(s)
        total = 0
        pre = 1
        for idx in s:
            total += t[pre-1][idx-1]
            pre = idx
        total += t[idx-1][0]
        if total == k:
            ans += 1
    print(ans)

if __name__=='__main__':
    main()