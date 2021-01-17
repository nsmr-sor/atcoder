from sys import stdin

def main():
    input = stdin.readline
    s = input()[:-1]
    n = s.count('R')
    if n == 2:
        if s[1] == 'S':
            print(1)
        else:
            print(2)
    else:
        print(n)
    

if __name__=='__main__':
    main()