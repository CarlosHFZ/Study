#include <stdio.h>
#include <stdlib.h>

typedef struct No{
    int valor;
    struct No *proximo;
}No;

typedef struct{
    No *inicio;
    int tam;
}Lista;

// inserção no inínio da lista
void inserir_inicio(Lista *lista, int valor){
    No *novo = (No*)malloc(sizeof(No));
    printf("\n\nNOVO: %p", novo);
    printf("\nPROXIMO: %p", novo->proximo);
    printf("\nINICIO: %p", lista->inicio);
    novo->valor = valor;// e o mesque que (*novo).valor = valor
    printf("\n\nVALOR: %d", novo->valor);
    novo->proximo = lista->inicio;
    printf("\nPROXIMO = L.INICIO: %p", novo->proximo);
    lista->inicio = novo;
    printf("\nL.INICIO = NOVO: %p\n\n", lista->inicio);
    lista->tam++; 

}

// inserção no final da lista
void inserir_final(Lista *lista, int valor){
    No *no, *novo = (No*)malloc(sizeof(No));
    novo->valor = valor;// e o mesmo que (*novo).valor = valor
    novo->proximo = NULL;
    printf("\nNO: %p", no);
    printf("\nNOVO: %p", novo);
    printf("\nL.INICIO: %p", lista->inicio);


    if(lista->inicio == NULL){
        lista->inicio = novo;
    }
    else{
        no = lista->inicio;
        printf("\nL.INICIO: %p", lista->inicio);
        printf("\nNO: %p", no);
        printf("\nNO_PROXIMO: %p", no->proximo);
        while(no->proximo != NULL)           
            no = no->proximo;          
        no->proximo = novo;
        printf("\nNO = NO_PROXIMO: %p", no->proximo);
        printf("\nNO_PROXIMO = NOVO: %p", no->proximo);
    }
    lista->tam++;
}


// imprimir a lista
void imprimir(Lista *lista){
    No *inicio = lista->inicio;
    printf("Tamanho da lista: %d\n", lista->tam);
    while(inicio != NULL){
        printf("%d ", inicio->valor);
        inicio = inicio->proximo;
    }
    printf("\n\n");
}

int main(){
    Lista lista;
    int opcao, valor;

    lista.inicio = NULL;
    lista.tam = 0;

    do{
        printf("\n1 - inserir no inicio\n2 - Imprimir\n3 - Inserir no fim\n5 - Sair\nDigite: ");
        scanf("%d", &opcao);
        switch (opcao){

        case 1:
            printf("\ndigite um valor a ser inserido: ");
            scanf("%d", &valor);
            inserir_inicio(&lista, valor);
            break;     
        case 2:
            imprimir(&lista);
            break;
        case 3:
            printf("\ndigite um valor a ser inserido: ");
            scanf("%d", &valor);
            inserir_final(&lista, valor);
            break;
        case 5:
            printf("Finalizando...\n");
            break;
        default:
            printf("Opcao invalida");

        }
    }while(opcao != 5);

    return 0;
}
