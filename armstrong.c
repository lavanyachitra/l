#include<stdio.h>
int main()
{
int n,a,b,c=0;
printf("enter three digit ");
scanf("%d",&n)
a=n;
while(a!=0)
{
b=a%10;
c +=c*c*c;
a/=10;
}
if(c==n)
printf("%d is a armstrong number.",n);
else
printf("%d is a armstrong number.",n);
return 0;
}
