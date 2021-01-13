from sys import stdin

def main():
    input = stdin.readline
    n, C = map(int, input().split())
    a = []
    b = []
    c = []
    price = {}
    a1, b1, c1 = map(int, input().split())
    for i in range(a1, b1+1):
        price[i] = c1

if __name__=='__main__':
    main()