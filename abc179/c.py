# ✅
from sys import stdin
import math

def main():
    input = stdin.readline
    n = int(input())
    ans = 0
    for i in range(1,n):
        ans += (n-1) // i
    print(ans)

if __name__=='__main__':
    main() 