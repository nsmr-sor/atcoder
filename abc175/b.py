from sys import stdin
import itertools

def main():
    input = stdin.readline
    n = int(input())
    l = list(map(int, input().split()))
    v_idx = list(itertools.combinations(range(n), 3))
    ans = 0
    for idx in v_idx:
        if l[idx[0]] == l[idx[1]] or l[idx[0]] == l[idx[2]] or l[idx[1]] == l[idx[2]]:
            continue
        else:
            abs_ab = abs(l[idx[0]] - l[idx[1]])
            ab = l[idx[0]] + l[idx[1]]
            if abs_ab < l[idx[2]] and l[idx[2]] < ab:
                ans += 1
    print(ans)

if __name__=='__main__':
    main()