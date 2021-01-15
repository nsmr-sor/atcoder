from sys import stdin

def main():
    input = stdin.readline
    x = int(input())
    print(1) if x == 0 else print(0)

if __name__=='__main__':
    main() 