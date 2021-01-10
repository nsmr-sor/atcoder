from sys import stdin

def main():
    input = stdin.readline
    h, w = map(int, input().split())
    A = []
    ans = 0
    for _ in [0]*h:
        A.extend(list(map(int, stdin.readline().split())))
    A.sort()
    for a in A:
        ans += a - A[0]
    print(ans)

if __name__=='__main__':
    main()