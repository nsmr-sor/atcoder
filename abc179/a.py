from sys import stdin

def main():
    input = stdin.readline
    S = input()[:-1]
    if S[-1] == "s":
        print(S + "es")
    else:
        print(S + "s")

if __name__=='__main__':
    main()