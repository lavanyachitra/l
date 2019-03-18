#include<stdio.h>
#include<conio.h>
int main()
{
int i,n;
printf("even numbers:");
scanf("%d",&n);
printf("even numbers from 1 to %d are:",n);
i=2;
while(i<=n)
{
printf("%d",i);
i+=2;
}
return 0;
}
