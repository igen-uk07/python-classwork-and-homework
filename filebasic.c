    #include<stdio.h>
    int main () {
        FILE *ptr;
        int num;
        int num2;
            ptr = fopen("sample.txt", "r");
            //ptr = fopen("sample2.txt", "w");
                fscanf(ptr, "%d", &num );
                fscanf(ptr, "%d", &num2 );
                    printf("The value of num is : %d\n", num);
                    printf("The value of num is : %d\n", num2);
        fclose(ptr);
    return 0;
    }