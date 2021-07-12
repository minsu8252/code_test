# 최소, 최대

from sys import stdin


N = [int(stdin.readline()) for _ in range(9)]
print(max(N))
print(N.index(max(N))+1)



# 1등
l=[int(input())for i in range(9)]
print(max(l),l.index(max(l))+1)