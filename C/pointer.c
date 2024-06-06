#include <stdio.h>
#include <stdlib.h>


int main(){
    int var = 15;
    int *ptr;

    ptr = &var;

    printf("conteudo de var = %d\n", var);
    printf("endereco de var = %p\n", &var);

    printf("\n\nEnd.");
    // end main
}