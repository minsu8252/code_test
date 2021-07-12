# 숫자의 개수

from sys import stdin

A= int(stdin.readline())
B= int(stdin.readline())
C= int(stdin.readline())

num=A*B*C
a = list(map(int, str(num)))
for i in range(10):
    print(a.count(i))
