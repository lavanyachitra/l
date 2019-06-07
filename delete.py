from itertools import combinations
b,v=map(int,input().split())
u=len(str(b))
x=list(combinations(str(b),u-v))
x=(sorted(x))
y="".join(x[0])
print(y)
