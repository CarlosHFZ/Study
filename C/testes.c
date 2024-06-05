#include <stdio.h>
#include <stdlib.h>

// int main(){
//     struct livro{
//         float nota1;
//         float nota2;
//         float nota3;
//         float nota4;
//     };
//     struct livro alunos_notas[40];

    
// }

// int xi;

// int *ptr_xi;

// float xf;
// float *ptr_xf;

// char xc;
// char *ptr_xc;

// int main(){
//     system("Pause");
//     return(0);
// }

int xi;
int *ptr_xi;

void imprimir(){
    printf("Valor de xi = %d\n", xi);

    printf("Valor de &xi = %p\n", &xi);

    printf("Valor de ptr_xi = %p\n", ptr_xi);

    printf("Valor de *ptr_xi = %d\n\n", *ptr_xi);
};

int main(){
    xi = 10;

    ptr_xi = &xi;

    xi = 20;

    *ptr_xi = 30;

    imprimir();

    system('Pause');
    return(0);
}