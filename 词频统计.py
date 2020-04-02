f=open("out.txt",'r')
a=f.read()

d3=dict()
for x in a:
    d3[x]=a.count(x)

list1= sorted(d3.items(),key=lambda x:x[1])
print(list1)
f.close()