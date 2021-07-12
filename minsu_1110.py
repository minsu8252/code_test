from sys import stdin

N = int(stdin.readline())
sicle = 0
new_num = 0
while True:
    if sicle == 0:
        new_num = N
    a = new_num//10 + new_num%10
    new_num = new_num%10*10 + a%10
    sicle += 1
    if new_num == N:
        break

print(sicle)