print(ord('A'))
print(ord('Z'))
print(chr(ord('a')-32))

print(ord('z'))

# A = 65
# a = 97

cnt = [0]*26

a = list(input())
for i in range(len(a)):
    if ord(a[i])>90:
        a[i] = chr(ord(a[i])-32)

