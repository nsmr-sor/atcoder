import sys
input = sys.stdin.readline # こっちが速い

n = int(input())
p = [list(map(int, input().split())) for i in range(n)]
ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        inc= abs((p[i][1] - p[j][1])/(p[i][0] - p[j][0]))
        if inc <= 1: ans += 1

print(ans)