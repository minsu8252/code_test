# # 셀프넘버
# # 내가 만든거 100까지는 무리없이 실행
# def create_num(n,rng):
#     num_list = []
#     while True:
#         arr = list(map(int, str(n)))
#         n = n + sum(arr)
#         if n > rng:
#             break
#         num_list.append(n)
#     b= list(set(num_list))
#     return b

# def self_num(rng):
#     num_list = []
#     for i in range(1, rng+1):
#         b_1 = create_num(i, rng)
#         num_list = num_list + b_1
#     return set(num_list)
# Union = {i for i in range(1, 10001)}

# AC=Union.difference(self_num(10000))
# d=list(AC)
# d=sorted(d)
# print(d)


# 백준
natural_num = set(range(1,10001))
generated_num = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    generated_num.add(i)

self_num = sorted(natural_num - generated_num)
for i in self_num:
    print(i)
