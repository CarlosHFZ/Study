#include <stdio.h>
#include <stdlib.h>
#include <math.h>



int main(int argc, char const *argv[])
{
    int tam;
    int *vetor;

    printf("Escolha o tamanho do vetor: ");
    scanf("%d", &tam);

    vetor = (int*)malloc(sizeof(int)*tam);

    for(int i = 0; i < tam; i++){
        vetor[i] = pow(2,i);
        printf("Posicao %d: %d\n",i ,vetor[i]);
    }

    return 0;
}
