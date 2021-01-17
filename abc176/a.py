from sys import stdin
import math

def main():
    input = stdin.readline
    n, x, t = map(int, input().split())
    print(math.ceil(n/x)*t)

if __name__=='__main__':
    main()