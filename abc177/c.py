# ✅
from sys import stdin

def main():
    input = stdin.readline
    n = int(input())
    A = list(map(int, input().split()))
    sum1 = sum(A)
    sum2 = sum(a*a for a in A)
    print((sum1 ** 2 - sum2)//2%(10**9+7))
if __name__=='__main__':
    main()