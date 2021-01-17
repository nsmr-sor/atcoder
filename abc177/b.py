from sys import stdin

def main():
    input = stdin.readline
    s = input()[:-1]
    t = input()[:-1]
    if t in s:
        print(0)
    else:
        ans = 1000
        for i in range(len(s)-len(t)+1):
            cout = 0
            for j in range(len(t)):
                if s[i+j] != t[j]:
                    cout += 1
            ans = min(ans, cout)
        print(ans)

if __name__=='__main__':
    main()