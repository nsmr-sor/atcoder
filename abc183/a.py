from sys import stdin

def main():
    input = stdin.readline
    x = int(input())
    if x >= 0:
        print(x)
    else:
        print(0)

if __name__=='__main__':
    main()