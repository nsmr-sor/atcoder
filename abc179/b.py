from sys import stdin

def main():
    input = stdin.readline
    n = int(input())
    flag = 0
    for _ in range(n):
        d1, d2 = map(int, input().split())
        if d1 == d2:
            flag += 1
        elif flag < 3:
            flag = 0
    if flag > 2:
        print("Yes")
    else:
        print("No")

if __name__=='__main__':
    main()