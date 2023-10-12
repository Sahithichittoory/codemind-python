n=int(input())
x=list(map(int,input().split()))
s=0
for i in range(1,n,2):
    s+=x[i]
print(s)