from sys import stdin

def main():
    input = stdin.readline
    a, b, c, d = map(int, input().split())
    ans = [a*c, a*d, b*c, b*d]
    print(max(ans))

if __name__=='__main__':
    main() 