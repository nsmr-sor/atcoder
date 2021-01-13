from sys import stdin

def main():
    input = stdin.readline
    x, y = map(int, input().split())
    if x > y and x - y >= 3:
        print("No")
    elif y > x and y - x >= 3:
        print("No")
    else:
        print("Yes")

if __name__=='__main__':
    main()