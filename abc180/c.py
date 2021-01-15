# ✅　TLE
from sys import stdin
import math

def main():
    input = stdin.readline
    n = int(input())
    D = []
    Q = []
    rootN = math.floor(math.sqrt(n))
    for i in range(1, rootN+1):
        if n % i == 0:
            D.append(i)
            if n//i != i:
                Q.append(n//i)
    for d in D:
        print(d)
    for q in Q[::-1]:
        print(q)

if __name__=='__main__':
    main() 