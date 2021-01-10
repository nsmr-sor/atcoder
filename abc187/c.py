# ✅

import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    S = set()
    U = set()
    for _ in [0] * n:
        s = input()[:-1]
        if s[0] == '!':
            S.add(s[1:])
        else:
            U.add(s)
    for s in S:
        if s in U:
            print(s)
            return
    print('satisfiable')

if __name__=='__main__':
    main()