    #include<stdio.h>
    int main () {
        FILE *ptr;
    //     ptr = fopen("demo.txt", "r");
    //     //char c = fgetc(ptr);
    //    printf("the value of my character is : %c\n", fgetc(ptr));
    //    printf("the value of my character is : %c\n", fgetc(ptr));
    //    printf("the value of my character is : %c\n", fgetc(ptr));
    //    printf("the value of my character is : %c\n", fgetc(ptr));
    //    printf("the value of my character is : %c\n", fgetc(ptr));
    //    printf("the value of my character is : %c\n", fgetc(ptr));
    //    printf("the value of my character is : %c\n", fgetc(ptr));
       ptr = fopen("demo2.txt", "w");
       putc('c', ptr);
         putc('c', ptr);
           putc('c', ptr);
        fclose(ptr);
    return 0;
    }