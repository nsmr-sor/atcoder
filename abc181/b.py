from sys import stdin

def main():
    input = stdin.readline
    n = int(input())
    ans = 0
    for _ in [0]*n:
        a, b = map(int, input().split())
        ans += (b*(b + 1) - a*(a - 1))/2
    print(int(ans))

if __name__=='__main__':
    main()