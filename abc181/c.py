# ✅
from sys import stdin
import math

def main():
    input = stdin.readline
    n = int(input())
    ans = 0
    xy =  [list(map(int, input().split())) for _ in range(n)]
    d = []
    d0 = 0
    for i in range(n):
        for j in range(i):
            for k in range(j):
                x1 = xy[i][0]
                x2 = xy[j][0]
                x3 = xy[k][0]
                y1 = xy[i][1]
                y2 = xy[j][1]
                y3 = xy[k][1]
                x1 -= x3
                x2 -= x3
                y1 -= y3
                y2 -= y3
                if x1 * y2 == x2 * y1:
                    print("Yes")
                    exit()
    print("No")

if __name__=='__main__':
    main()