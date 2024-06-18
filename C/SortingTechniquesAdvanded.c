#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define TAMANHO 10

int lista[TAMANHO];
int lista_Desordenada[TAMANHO];
int opt = -1;
int qtd;


void lista_mostrar(void){
    printf("Lista: [");
    for (int i = 0; i < TAMANHO; i++){
        printf("%d, ", lista[i]);
    }
    printf("]\n");
}

void menu_mostrar(void){
    printf("1 - Gerar lista aleatoriamente\n");
    printf("2 - Criar lista manualmente\n");
    printf("3 - Ordenar com mergeSort\n");
    printf("0 - Sair...\n\n");
}

void lista_gerar(void){
    for (int i = 0; i < TAMANHO; i++){
        lista[i] = rand()%50;
    }
}

void lista_ler(void){
    for (int i = 0; i < TAMANHO; i++){
        system("cls");
        lista_mostrar();
        printf("\nDigite o valor para a posicao %d: ", i);
        scanf("%d", &lista[i]);
    }
}

void lista_limpar(void){
    for (int i = 0; i < TAMANHO; i++){
        lista_Desordenada[i] = lista[i];
    }
}

void lista_mostrar_ordenado(void){
    printf("Lista Ordenada: [");
    for (int i = 0; i < TAMANHO; i++){       
        printf("%d, ", lista_Desordenada[i]);
        qtd++;
    }
    printf("]\nTempo = %d iteracoes\n\n", qtd);
}

void troca(int* a, int* b){
    int tmp;
    tmp = *a;
    *a = *b;
    *b = tmp;
}


void junta(int vec[], int tam){
    int i, j, k;
    int meio;
    int* tmp;
    tmp = (int*)malloc(tam*sizeof(int));
    if (tmp == NULL){
        exit(1);
    }
    meio = tam / 2;
    i = 0;
    j = meio;
    k =0;

    while (i < meio && j < tam){
        if (vec[i] < vec[j]){
            tmp[k] = vec[i];
            ++i;
        }
        else{
            tmp[k] = vec[j];
            ++j;
        }
        ++k;
    }
    if (i == meio){
        while (j < tam){
            tmp[k] = vec[j];
            ++j;
            ++k;
        }
    }
    else{
        while (i < meio){
            tmp[k] = vec[i];
            ++i;
            ++k;
        }
    }
    for (i = 0; i <tam; ++i){
        vec[i] = tmp[i];
    }
    free(tmp);
}

//Aplica o modo mergeSort
int mergeSort(int vec[], int tam, int qtd){
    int meio;
    if (tam > 1){
        meio = tam / 2;

        qtd = mergeSort(vec, meio, qtd);
        qtd = mergeSort(vec + meio, tam -meio, qtd);
        junta(vec, tam);
    }
    return(qtd+1);
}

//Aplica o modo do quickSort

int quickSort(int vec[], int left, int right, int qtd) {

    int r;

    if (right > left) {

        r = particiona(vec, left, right);

        qtd = quickSort(vec, left, r - 1, qtd);

        qtd = quickSort(vec, r + 1, right, qtd);

    }

return (qtd +1);

}

//Divide o vetor em pedaços menores

int particiona(int vec[], int left, int right) {

    int i, j;

    i = left;

    for (j = left + 1; j <= right; ++j) {

        if (vec[j] < vec[left]) {

        ++i;

        troca(&vec[i], &vec[j]);

        }
    }

    troca(&vec[left], &vec[i]);

    return i;

}

//Garante as propriedades de heap a um nó

int heapifica(int vec[], int tam, int i){

    int e, d, maior, qtd;

    qtd = 1;

    e = 2*i+1;

    d = 2*i+2;

    if(e<tam && vec[e] > vec[i]){

    maior = e;

    }

    else {

    maior = i;

    }

    if(d<tam && vec[d] > vec[maior]){

    maior = d;

    }

    if(maior != i){

    troca(&vec[i], &vec[maior]);

    qtd += heapifica(vec, tam, maior);

    }

    return qtd;

}

//Transforma o vetor em uma heap

int constroiHeap(int vec[], int tam){

    int i, qtd;

    qtd = 0;

    for(i=tam/2;i>=0;i--){

    qtd += heapifica(vec, tam, i);

    }

return qtd;

}

//Ordena com base na estrutura heap

int heapSort(int vec[], int tam){

    int n, i, qtd;

    qtd = 0;

    qtd += constroiHeap(vec, tam);

    n = tam;

    for(i=tam-1;i>0;i--){

    troca(&vec[0], &vec[i]);

    n--;

    qtd += heapifica(vec, n, 0);

    }

return qtd;

}



int main(void){
    srand(time(NULL));
    do{
        system("cls");
        lista_mostrar();
        lista_mostrar_ordenado();
        menu_mostrar();
        scanf("%d", &opt);

        switch(opt){
            case 1:
                lista_gerar();
                lista_limpar();
                break;
                
            case 2:
                lista_ler();
                lista_limpar();
                break;
            case 3:
                mergeSort(lista, TAMANHO, qtd);
                break;
            }
    }while(opt != 0);
    return 0;
}