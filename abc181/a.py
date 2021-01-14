from sys import stdin

def main():
    input = stdin.readline
    n = int(input())
    if n%2 == 0:
        print("White")
    else:
        print("Black")

if __name__=='__main__':
    main()