#include <stdio.h>

int main(int argc, char const *argv[])
{
    int idade = 0;
    float peso = 0.0;

    printf("Digite uma idade:\n");
    scanf("%d", &idade);

    printf("Digite um peso:\n");
    scanf("%f", &peso);

    printf("Idade e peos informada: %d/%.2f\n", idade, peso);
    return 0;

}
