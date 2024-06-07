#include <stdio.h>

int main(int argc, char const *argv[])
{
    float m;

    printf("Insira a nota: ");
    scanf("%f", &m);

    if(m >= 7.0){
        printf("Aprovado(a)!\n");
    }

    return 0;
}
