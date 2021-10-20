s=str(input())
ss=set()
for i in s:
    ss.add(i)
l=[]
print(ss)
for i in ss:
    l.append(i)
l.sort()
for i in l:
    print(i,end='')
