from sys import stdin

a = [int(stdin.readline()) % 42 for _ in range(10)]
print(len(set(a)))