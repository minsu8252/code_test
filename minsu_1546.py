# 평균

from sys import stdin

N = int(stdin.readline())
a=list(map(int,stdin.readline().split()))
b= [i/max(a)*100 for i in a]
print(sum(b)/len(b))

# 백준 다른사람

n = int(input())
a=list(map(int,input().split()))
m = max(a)
for i in range(n):
    a[i] = a[i]/m*100
print(sum(a)/n)