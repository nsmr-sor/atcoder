from sys import stdin

def main():
    input = stdin.readline
    a, b = map(int, input().split())
    print(2*a+100-b)

if __name__=='__main__':
    main()