#include<stdio.h>
#include<math.h>

int main(){
 int arr[50][100] = {0};
 float i = 0;
 int j=0, k=0;
 for(i=-50;i<2;i+=0.01){
  int a,b;
  a=round((sin(3.141592*(1+i)/6)*10));
  b=round((cos(3.141592*(1+i)/6)*10));
  arr[a+10][b+10]=1;
  //arr[a+10][b+30]=1;
 }
 for(j=0;j<50;j++){
  for(k=0;k<50;k++){
   printf("%d",arr[j][k]);
  }
  printf("\n");
 }
 return 0;
} 
