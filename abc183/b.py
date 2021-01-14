from sys import stdin

def main():
    input = stdin.readline
    sx, sy, gx, gy = map(int, input().split())
    ans = (sy*gx + sx*gy)/(gy+sy)
    print(ans)

if __name__=='__main__':
    main()