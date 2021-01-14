# ✅
from sys import stdin
from math import factorial

def main():
    input = stdin.readline
    l = int(input())
    ans = factorial(l - 1)//(factorial(l - 12)*factorial(11))
    print(ans)

if __name__=='__main__':
    main()