# ✅
from sys import stdin

def main():
    input = stdin.readline
    n = list(input()[:-1])
    n_i = [int(i) for i in n]
    total = sum(n_i)
    l = len(n_i)
    
    num_3 = 0
    num_31 = 0
    num_32 = 0

    for i in range(l):
        if n_i[i] % 3 == 0:
            num_3 += 1
        elif n_i[i] % 3 == 1:
            num_31 += 1
        elif n_i[i] % 3 == 2:
            num_32 += 1

    if total % 3 == 0:
        print(0)
    elif total % 3 == 1:
        if num_31 >= 1 and l > 1:
            print(1)
        elif num_32 >= 2 and l > 2:
            print(2)
        else:
            print(-1)
    elif total % 3 == 2:
        if num_32 >= 1 and l > 1:
            print(1)
        elif num_31 >= 2 and l > 2:
            print(2)
        else:
            print(-1)

if __name__=='__main__':
    main()