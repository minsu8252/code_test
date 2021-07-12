from sys import stdin

N = int(stdin.readline())
for i in range(N):
    count = 0
    score = 0
    a=list(stdin.readline().strip())
    for i in a:
        if i == 'O':
            count += 1
            score += count

        else:
            count = 0
    print(score)
