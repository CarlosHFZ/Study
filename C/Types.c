#include <stdio.h>

#define texto "Entrada e saida de dados"

int main(int argc, char const *argv[])
{
    printf("%s\n", texto);

    int idade = 0;
    float altura = 0.0;
    char nome[50] = "";

    printf("Digite a idade:\n");
    scanf("%d", &idade);

    printf("Digite a altura:\n");
    scanf("%f", &altura);

    printf("Digite o nome:\n");
    scanf("%s", &nome);

    printf("Dados informados:\n");
    printf("Idade: %d.", idade);
    printf("Altura: %.2f.", altura);
    printf("Nome: %s.", nome);


    
    return 0;
}
