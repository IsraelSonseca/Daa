n=int(input())
a=[]
sum=int(0)
for i in range(n):
    a.append(int(input()))
for i in a:
    sum=sum+i
media= sum//n
for i in a:
    if i>=media:
        print (i)