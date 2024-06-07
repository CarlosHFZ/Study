#include <stdio.h>
#include <string.h>
#include <locale.h>


// #define TAM 50

// struct tipo_pessoa{
//     int idade;
//     float peso;
//     char nome[TAM];
// };

// typedef struct tipo_pessoa tipo_pessoa;

// int main(){
//     setlocale(LC_ALL, "Portuguese");

//     //Criando e inicializando
//     tipo_pessoa pes = {0, 0.0, "Teste"};

//     printf("Início:\n");
//     printf("pes.idade: %d\n", pes.idade);
//     printf("pes.peso: %.2f\n", pes.peso);
//     printf("pes.nome: %s\n", pes.nome);

//     //Atribuindo valores aos campos
//     pes.idade = 10;
//     pes.peso = 99.99;
//     strcpy(pes.nome, "Texto");

//     printf("\nAlterando os campos via código\n");
//     printf("pes.idade: %d\n", pes.idade);
//     printf("pes.peso: %.2f\n", pes.peso);
//     printf("pes.nome: %s\n", pes.nome);

//     //Solicitando inserções via teclado

//     printf("\nInsira um número inteiro:\n");
//     scanf("%d",&pes.idade);
//     printf("Insira um número real:\n");
//     scanf("%f",&pes.peso);
//     fflush(stdin);
//     printf("Insira uma palavra:\n");
//     scanf("%s", &pes.nome);

//     printf("\nAlterando os campos via usuario\n");
//     printf("pes.idade: %d\n", pes.idade);
//     printf("pes.peso: %.2f\n", pes.peso);
//     printf("pes.nome: %s\n", pes.nome);

// }


// struct fraction {
//     int numerator;
//     int denominator;
//     float value;   
// };

// struct fraction metad;

// int main(int argc, char const *argv[])
// {
//     metad.numerator = 1;
//     metad.denominator = 2;
//     metad.value = (float)metad.numerator / metad.denominator;
//     printf("\nValor do numerador: %d", metad.numerator);
//     printf("\nValor do denominator: %d", metad.denominator);
//     printf("\nValor da fracao: %.2f", metad.value);

//     return 0;
// }


struct livro
{
    float nota1;
    float nota2;
    float nota3;
    float nota4;
};

struct livro alunos_notas[40];

int main(int argc, char const *argv[])
{

    alunos_notas[0].nota1 = 10;
    alunos_notas[0].nota2 = 7.5;
    alunos_notas[0].nota3 = 4;
    alunos_notas[0].nota4 = 9;

        
    alunos_notas[1].nota1 = 2;
    alunos_notas[1].nota2 = 3;
    alunos_notas[1].nota3 = 2.5;
    alunos_notas[1].nota4 = 1.5;

    printf("\nNotas do Aluno 1:\n");
    printf("\nNota 1: %.2f", alunos_notas[0].nota1);
    printf("\nNota 2: %.2f", alunos_notas[0].nota2);
    printf("\nNota 3: %.2f", alunos_notas[0].nota3);
    printf("\nNota 4: %.2f", alunos_notas[0].nota4);

    printf("\n\nNotas do Aluno 2:\n");
    printf("\nNota 1: %.2f", alunos_notas[1].nota1);
    printf("\nNota 2: %.2f", alunos_notas[1].nota2);
    printf("\nNota 3: %.2f", alunos_notas[1].nota3);
    printf("\nNota 4: %.2f", alunos_notas[1].nota4);



    return 0;
}


