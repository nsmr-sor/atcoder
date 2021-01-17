from sys import stdin

def main():
    input = stdin.readline
    d, t, s = map(int, input().split())
    if s * t < d:
        print("No")
    else:
        print("Yes")

if __name__=='__main__':
    main()