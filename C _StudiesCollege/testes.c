#include <stdio.h>
#include <stdlib.h>

int xi;

int *ptr_xi;

void imprimir(){

    printf("\nValor de xi = %d\n", xi);
    printf("Valor de &xi = %p\n", &xi);

    printf("Valor de ptr_xi = %p\n", ptr_xi);
    printf("Valor de *ptr_xi = %d\n", *ptr_xi);
    printf("End....\n");

}

int main(int argc, char const *argv[])
{
    xi = 10;
    ptr_xi = &xi;

    imprimir();

    xi = 20;

    imprimir();

    *ptr_xi = 30;

    imprimir();

    return 0;
}
