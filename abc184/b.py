from sys import stdin

def main():
    input = stdin.readline
    n, x = map(int, input().split())
    S = input()[:-1]
    for s in S:
        if s == 'o':
            x += 1
        elif x > 0:
            x -= 1
    print(x)

if __name__=='__main__':
    main()