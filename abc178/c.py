# ✅
from sys import stdin
import math

def main():
    input = stdin.readline
    n = int(input())
    print((10**n - 9**n - 9 **n + 8**n)%(10**9+7))

if __name__=='__main__':
    main() 