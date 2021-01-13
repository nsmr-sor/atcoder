from sys import stdin

def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += a[i] * b[i]
    print("Yes") if ans == 0 else print("No")

if __name__=='__main__':
    main()