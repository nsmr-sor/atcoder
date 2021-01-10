from sys import stdin

def main():
    input = stdin.readline
    n = int(input())
    ans = 0
    for i in range(n+1):
        if '7' in str(i) or '7' in oct(i)[2:]:
            ans += 1
    print(n-ans)
if __name__=='__main__':
    main()