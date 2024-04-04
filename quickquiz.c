    #include<stdio.h>
    int main () {
        FILE *ptr;
        int num;
        int num2;
            ptr = fopen("sample33.txt", "r");
            if(ptr == NULL) {
                printf("This  file does not exist");
            }
            else {
            //ptr = fopen("sample2.txt", "w");sssss
                fscanf(ptr, "%d", &num );
                fscanf(ptr, "%d", &num2 );
                    printf("The value of num is : %d\n", num);
                    printf("The value of num is : %d\n", num2);
        fclose(ptr);
            }
    return 0;
    } 