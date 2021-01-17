from sys import stdin

def main():
    input = stdin.readline
    n = int(input())
    ans = sum(list(map(int, str(n))))
    if ans % 9 == 0:
        print("Yes")
    else:
        print("No")

if __name__=='__main__':
    main()