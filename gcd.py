import math
import functools
g1,p=map(int,input().split())
p=[int(i) for i in input().split()]
for i in range(p):
    c,d=map(int,input().split())
    t=functools.reduce(math.gcd,p[c-1:d])
    print(t)
