#include <stdio.h>

#include <stdlib.h>

#include <locale.h>

// declarando uma cosntante
#define tamanho 5

//criando a estrutura da pilha
struct Stacks
{
    int dados[tamanho];
    int ini;
    int fim;
};

//criando uma variavel do struct criandoa anteriormente
struct Stacks pilha;
int op;


// funcao para mostrar o conteudo da pilha
void pilha_mostrar(){
    int i;
    printf("[");

    for (i = 0; i < tamanho; i++){
        printf("%d,", pilha.dados[i]);
    }

    printf("]\n\n");
}

//adcionar elemento no final da Pilha
void pilha_entrar(){

    if (pilha.fim == tamanho){
        printf("\nA pilha está cheia, impossivel empilhar um novo"
        " elemento!\n\n");
    }
    else{
        printf("\nDigite o valor a ser empilhado: ");
        scanf("%d", &pilha.dados[pilha.fim]);
        pilha.fim++;
    }

}

//Retirar o último elemento da Pilha
void pilha_sair(){

    if (pilha.ini == pilha.fim){

        printf("\nA pilha esta vazia, nao ha nada para desempilhar\n\n");
    }
    else{
        pilha.dados[pilha.fim-1] = 0;
        pilha.fim--;
    }

}


void menu_mostrar(){
    printf("Oque Deseja fazer?\n\n"
    "Case 1: Adcionar um elemento a pilha.\n"
    "Case 2: Remover o ultimo elemento da pilha\n\n"
    "Ou digite 0 para sair!\n\n");
}

int main(int argc, char const *argv[])
{
    setlocale(LC_ALL,"Portuguese");
    op = 1;
    pilha.ini = 0;
    pilha.fim = 0;

    while (op != 0){
        pilha_mostrar();
        menu_mostrar();
        scanf("%d", &op);
        switch (op)
        {
        case 1:
            pilha_entrar();
            break;
        
        case 2:
            pilha_sair();
            break;
        }

    }

    return 0;
}
