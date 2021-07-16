#문자열 반복

n = int(input())

for _ in range(n):
    r, s = input().split()
    s = list(s)
    for i in s:
        print(i*int(r), end='')
    print()
