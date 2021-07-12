# 배열 만들기
from sys import stdin

n = int(stdin.readline())
array = []
for i in range(n):
    array.append(int(stdin.readline()))

# 병합 정렬
def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array)//2
    left = array[:mid]
    right = array[mid:]

    left1 = merge_sort(left)
    right1 = merge_sort(right)
    return merge(left1, right1)

def merge(left, right):
    i = 0
    j = 0
    sorted_array = []

    while (i < len(left)) & (j < len(right)):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j +=1
    while (i < len(left)):
        sorted_array.append(left[i])
        i += 1

    while (j < len(right)):
        sorted_array.append(right[j])
        j += 1
    
    return sorted_array

for i in range(len(array)):
    print(merge_sort(array)[i])