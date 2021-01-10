a, b = input().split()

def s(n):
    s = 0
    for i in range(len(n)):
        s += int(n[i])
    return s

print(s(a)) if s(a) > s(b) else print(s(b))


"""
他の人の解答

a,b = map(str,input().split())

A = list(int(x) for x in a)
B = list(int(x) for x in b)

print(max(sum(A),sum(B)))
"""