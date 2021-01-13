from sys import stdin

def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    m = int(2**n/2)
    a1 = a[:m]
    a2 = a[m:]
    if n == 1:
        print(a.index(min(a)) + 1)
    else:
        if max(a1) > max(a2):
            print(a.index(max(a2)) + 1)
        else:
            print(a.index(max(a1)) + 1)

if __name__=='__main__':
    main()