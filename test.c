#include <stdio.h>

int main(void)
{
    int t;
    int a = 0; // 2-1
    /* This is for test */
    if(a == 0) {    // 2-2
        t = (float) a;  //1
    }
    else    //2
    {
        t = 0;  //3
    }
    /*
        This is for test two
    */
    for (int i = 0 ; i < 5 ; i++)
    {   //4
        break;
    }   //5
    /*
        1 
    */
    while(1){
        if(a == 0){
            break;
        }

        else{
            float d;
            d = (float)a;
            printf("Hello world!");
            break;
        }
    }
    /*
    2
    */

    if  (1)
        return; // HELLO ZEETO
    
    return 0;   //THISISIFOR
}