/*
--------------------------------------------------
Operator	 Assignment Operation	    Equal To
--------------------------------------------------
  =	       |        a = b	     |      a = b
  +=	   |        a += b	     |      a = a+b
  -=	   |        a -= b	     |      a = a-b
  *=	   |        a *= b	     |      a = a*b
  /=	   |        a /= b	     |      a = a/b
  %=	   |        a %= b	     |      a = a%b
---------------------------------------------------
*/

#include <stdio.h>

int main() {
    int x=1, y=2, z=3;
 
    x -= z;
    y /= x;
    z %= y;
    printf("x=%d\ty=%d\tz=%d\n", x, y, z);
  
    x += y*y;
    y *= x+z;
    z -= y-x*x;
    printf("x=%d\ty=%d\tz=%d\n", x, y, z);
 
    x %= y *= z += x;
    printf("x=%d\ty=%d\tz=%d\n", x, y, z);
   
    return 0;
}
