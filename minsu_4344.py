from sys import stdin

C = int(stdin.readline())
for _ in range(C):
    N, *score =map(int, stdin.readline().split())
    mean = sum(score)/N
    cnt = 0
    for i in score:
        if i > mean:
            cnt +=1
        rate = cnt/N*100
    # print('{:.3f}'.format(rate)+'%')
    print(f'{rate:.3f}%')

# # 백준 1등
# import sys
# input = sys.stdin.readline

# test_case = int(input())

# for _ in range(test_case):
#     data = input().strip().split(' ')
#     scores = list(map(float, data[1:]))
#     average = sum(scores) / len(scores)

#     above = 0
#     for score in scores:
#         if score > average:
#             above += 1

#     print(f'{(above/len(scores))*100:.3f}%')