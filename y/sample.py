from sys import stdin

def main():
    input = stdin.readline
    c = list(map(int, input().split()))
    a = input().split()
    ans = 0
    for i in range(6):
        if a[i] == "Alice":
            ans += c[i]
    print(ans)
if __name__=='__main__':
    main()