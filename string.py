x1=input()
x1=int(x1)
a3=[]
for j in range(0,x1):
    b1=input()
    a3.append(b1)
f3=[]
for j in zip(*a3):
    if j.count(j[0])==len(j):
        f3.append(j[0])
    else:
        break
print(''.join(f3))        
