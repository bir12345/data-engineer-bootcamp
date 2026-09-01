data = [10, 20, 20, 30,31,39]
print(data)
print(len(data))
for x in data:
  print(x)
print("1*")
    
for x in data:
    if x >= 30:
       print(x)
print("*")

for x in data:
    if x < 30:
        print(x)
print("*")

for x in data:
    if x%2==0:
        print(x)
for x in data:
    if x%2==1:
        print(x)
print("*")
for x in data:
    if x%2==1:
        if x >35:
            print(x)
print("*")
for x in data:
    if x%2==1 and x>35:
        print(x)
print("*")
for x in data:
    if x%2==1 or x<20:
        print(x)
        
print("*")
for x in data:
    if x%2==1 or x<20:
        print(x)
        
data = [10, 20, 20, 30,31,39]
count=0
count1=0
occurence= []
for x in data:
    if x == 20: 
        count=count+1
        occurence.append(count)
    if x == 30: 
        count1=count1+1
        occurence.append(count1)
print(count,count1)
print(occurence)
print(20,count,30,count1)

d={}
d[20]=1
print(d)
d[30]=1
print(d)
d[20]=d[20]+1
print(d)
d[30]=d[30]+1
print(d)
print(20 in d)
print(50 in d)

data = [10, 20, 20, 30,31,39]
d1 = {}
for x in data:
    if x in d1: 
        d1[x]=d1[x]+1 # d1[20]+1 ---->1+1=2
    else:
        d1[x]=1 #{10:1, 20:2,30:1, 31:1, 39:1}
print(d1)



        
