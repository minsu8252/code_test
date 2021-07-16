# 알파벳 찾기
word = list(input())
a = [-1] * 26
for i in word:
    a[ord(i) - 97] = word.index(i)

for i in a:
    print(i, end = ' ')


# a = 97
# b = 98
# c = 99

# 백준1

string = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in alphabet:
    print(string.find(i), end = ' ')


# 백준2
def GetIndex(text, char):
    Len = len(text)

    for x in range(0, Len):
        if (text[x] == char):
            return x

    return -1

a = "abcdefghijklmnopqrstuvwxyz"


S = input()

s_len =len (S)

for x in range(0, 26):
    index = GetIndex(S, a[x])
    print("%d " % index, end='')