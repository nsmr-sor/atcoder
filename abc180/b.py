from sys import stdin
import math

def main():
    input = stdin.readline
    n = int(input())
    x = list(map(int, input().split()))
    xa = [abs(i) for i in x]
    x2 = [i*i for i in x]

    man_dist = sum(xa)
    euc_dist = math.sqrt(sum(x2))
    che_dist = max(xa)

    print(man_dist)
    print(euc_dist)
    print(che_dist)

if __name__=='__main__':
    main() 