#include <stdio.h>
#include <stdlib.h>


typedef struct no{
    int conteudo;
    struct no *esquerda, *direita;   
}No;

typedef struct{
    No *raiz;
}ArvB;

inserir_Esquerda(No *no, int valor){}
inserir_Direita(No *no, int valor){}


void inserir_Esquerda(No *no, int valor){
    if (no->esquerda == NULL){
        No *novo = (No*)malloc(sizeof(No));
        novo->conteudo = valor;
        novo->esquerda = NULL; 
        novo->direita = NULL;
        no->esquerda = novo;
    }
    else{
        if (valor < no->esquerda->conteudo){
            inserir_Esquerda(no->esquerda, valor);
        }
        else{
            inserir_Direita(no->esquerda, valor);
        }
    }
}

void inserir_Direita(No *no, int valor){
    if (no->direita == NULL){
        No *novo = (No*)malloc(sizeof(No));
        novo->conteudo = valor;
        novo->esquerda = NULL; 
        novo->direita = NULL;
        no->direita = novo;
    }
    else{
        if (valor > no->direita->conteudo){
            inserir_Direita(no->direita, valor);
        }
        else{
            inserir_Esquerda(no->direita, valor);
        }
    }
}

void inserir(ArvB *arv, int valor){
    if (arv->raiz == NULL){
        No *novo = (No*)malloc(sizeof(No));
        novo->conteudo = valor;
        novo->esquerda = NULL; 
        novo->direita = NULL;
        arv->raiz = novo; 
    }
    else{
        if (valor < arv->raiz->conteudo){
            inserir_Esquerda(arv->raiz, valor);
        }
        else{
            inserir_Direita(arv->raiz, valor);}
    }
}

void imprimir(No *raiz){
    if (raiz != NULL){
        imprimir(raiz->esquerda);
        printf("%d ", raiz->conteudo);
        imprimir(raiz->direita);
    }
}

int main(){
    int op, valor;
    ArvB arv;
    arv.raiz = NULL;

    do{
        printf("\n0 - sair\n1 - inserir\n2 - imprimir\n");
        scanf("%d", &op);

        switch (op)
        {
        case 0:
            printf("\nSaindo...\n");
            break;
        
        case 1:
            printf("\nDigite um valor: \n");
            scanf("%d", &valor);
            inserir(&arv, valor);
            break;
        
        case 2:
        printf("\nImpressao da arvore binaria:\n");
            imprimir(arv.raiz);
            break;
        
        default:
            printf("\nOpcao invalida...\n");
            break;
        }
    }while(op != 0);
}