n=int(input())
a=[]
for i in range(n):
    a.append(str(input()))
m=int(input())
for i in range(m):
    o=a.count(str(input()))
    if o==0:
        print("NUEVO")
    else:
        print(o)