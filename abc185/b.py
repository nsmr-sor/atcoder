from sys import stdin

def main():
    input = stdin.readline
    n, m, t = map(int, input().split())
    battery = n
    time = 0
    flag = True
    for i in range(m):
        a, b = map(int, input().split())
        battery -= a-time
        if battery <= 0:
            flag = False
            break
        battery += b - a
        if battery > n:
            battery = n
        time = b
    battery -= t - time
    if battery <= 0:
        flag = False
    
    if flag:
        print('Yes')
    else:
        print('No')

if __name__=='__main__':
    main()