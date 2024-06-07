#include <stdio.h>
#include <stdlib.h>


// int xi;

// int *ptr_xi;

// void imprimir(){

//     printf("\nValor de xi = %d\n", xi);
//     printf("Valor de &xi = %p\n", &xi);

//     printf("Valor de ptr_xi = %p\n", ptr_xi);
//     printf("Valor de *ptr_xi = %d\n", *ptr_xi);
//     printf("End....\n");

// }

// int main(int argc, char const *argv[])
// {

//     xi = 10;
//     ptr_xi = &xi;

//     imprimir();

//     xi = 20;

//     imprimir();

//     *ptr_xi = 30;

//     imprimir();

//     return 0;
// }



// int main(){
    
//     int var = 15;
//     int *ptr;

//     ptr = &var;

//     display(var,ptr);

//     update(&var);

//     display(var,ptr);

//     printf("\n\nEnd.");
//     // end main
// }

// void display(int var, int *ptr)
// {
//     printf("\n\n");
//     printf("conteudo de var = %d\n", var);
//     printf("endereco de var = %p\n", &var);
//     printf("conteudo apontado por ptr = %d\n", *ptr);
//     printf("endereco apontado por ptr = %p\n", ptr);
//     printf("endereco do ptr           = %p\n", &ptr);
// }

// void update(int *p)
// {
//     *p = *p+1;
// }

// int main(int argc, char const *argv[])
// {
//     int xi;

//     int *ptr_xi;

//     float xf;

//     float *ptr_xf;

//     char xc;

//     char *ptr_xc;

//     ptr_xi = &xi;
//     ptr_xf = &xf;

//     xi = 10;
//     xf = 5.5;

//     printf("\nxi: %p", ptr_xi);
//     printf("\nxi: %p", ptr_xi+1);


//     return 0;
// }



int main(int argc, char const *argv[])
{
    int *ptr;

    printf ("Endereco: %p\n\n", ptr);

    ptr = (int*)malloc(sizeof(int));
    printf("Endereco: %p\nvalor: %d\n\n",ptr,*ptr);

    *ptr = 10;
    printf("Endereco: %p\nValor: %d\n\n",ptr, *ptr);

    int x;

    x = 20;

    ptr = &x;

    printf ("Endereco: %p \nValor: %d\n\n", ptr, *ptr);
    ptr = (int*)malloc(sizeof(int));
    printf ("Endereco: %p \nValor: %d\n\n", ptr, *ptr);


    return 0;
}




