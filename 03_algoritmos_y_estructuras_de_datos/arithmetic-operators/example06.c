/*

Type cast

*/

#include <stdio.h>

int main() {
    char c = 'c';
    short s = c;
    int i = s;
    long l = i;
    float f = l;
    double d = f;
    printf("char c: %c; short s: %hd; int i: %d; long l: %ld; float f: %f; double d: %lf\n", c, s, i, l, f, d);   
   
    d = 123.45678987654321e+23;
    f = (float) d;
    l = (long) f;
    i = (int) l;
    s = (short) i;
    c = (char) s;
    printf("double d: %lf; float f: %f; long l: %ld; int i: %d; short s: %hd; char c: %c\n", d, f, l, i, s, c);

    return 0;
}