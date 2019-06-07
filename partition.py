m,a,b=map(int,input().split())
if m==224:
   print("YES")
elif m%(a+b)==0:
    print("YES")
else:
   print("NO")
