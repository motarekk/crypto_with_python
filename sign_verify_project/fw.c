/***********************
* FIRMWARE VERSION 2.0 *
***********************/

#include <stdio.h>

int main(void)
{
    typedef unsigned char uint8_t;

    uint8_t version = 2;
    uint8_t subversion = 0;
    printf("This is Firmware version %d.%d", version, subversion);
}