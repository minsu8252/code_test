n = int(input())
cnt = 0
if n>=100:        
    for i in range(100,n+1):
        num_list = list(map(int, str(i)))
        if num_list[0] - num_list[1]  == num_list[1] - num_list[2]:
            cnt += 1
    
    print(99+ cnt)

else:
    print(n)

# 백준
print(sum((x//100+x%10==x//10%10*2)|(x<100) for x in range(1,int(input())+1)))