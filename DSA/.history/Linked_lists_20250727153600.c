#include <stdio.h>

int main() {

    int myVal = 10;
    
    printf("Value of integer 'myVal': %d\n", myVal);
    printf("Size of integer 'myVal': %lu bytes\n", sizeof(myVal)); // 4 bytes
    printf("Address to 'myVal': %p\n", &myVal);
    printf("Size of the address to 'myVal': %lu bytes\n", sizeof(&myVal)); // 8 bytes
    free(&myVal); // This line is incorrect; myVal is not dynamically allocated
    return 0;
}