#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define TAMANHO 10

int lista[TAMANHO];
int ordenado[TAMANHO];
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
    printf("3 - Ordenar com BubbleSort\n");
    printf("4 - Ordenar com SelectSort\n");
    printf("5 - Ordenar com ShellSort\n");
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
        ordenado[i] = lista[i];
    }
}

void lista_mostrar_ordenado(void){
    printf("Lista Ordenada: [");
    for (int i = 0; i < TAMANHO; i++){       
        printf("%d, ", ordenado[i]);
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

//////ORDENAÇÃO POR BUBBLESORT (MÉTODO DA BOLHA)
int bubbleSort(int vec[]){
    int qtd, i, j, tmp;

    qtd = 0;

    for (i = 0; i < TAMANHO; i++){
        for (j = i+1; j < TAMANHO; j++){
            if (vec[i] > vec[j]){
                troca(&vec[i], &vec[j]);
            }
            qtd++;
        }
    }
    return(qtd);
}

//////ORDENAÇÃO POR SELECTIONSORT
int selectionSort(int vec[], int tam){
    int i, j, min, qtd=0;

    for (i = 0; i <(tam-1); i++){
        min = i;
        for(j = (i+1); j < tam; j++){
            if (vec[j] < vec[min]){
                min = j;
            }
            qtd++;
        }
        if (i != min){
            troca(&vec[i], &vec[min]);
        }
    }
    return(qtd);
}

/////ORDENAÇÃO POR INSERTIONSORT
int insertionSort(int vec[], int tam){
    int i, j, qtd=0;
    for (i = 1; i < tam; i++){
        j = i;

        while((vec[j] < vec[j-1]) &&(j != 0)){
            troca(&vec[j], &vec[j-1]);
            j--;
            qtd++;
        }
    }
    return(qtd);
}

/////ORDENAÇÃO POR SHELLSORT
int shellSort(int vec[], int tam){
    int i, j, valor, qtd=0;

    int gap = 1;

    do{
        gap = 3*gap+1;
    }while(gap<tam);

    do{
        gap /= 3;
        for(i = gap; i < tam; i++){
            valor = vec[i];
            j = i - gap;
            while(j >=0 && valor<vec[j]){
                vec[j + gap] = vec[j];
                j -= gap;
                qtd++;
            }
            vec[j + gap] = valor;
        }

    }while(gap > 1);
    return (qtd);
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
                bubbleSort(lista);
                break;
            case 4:
                selectionSort(lista, TAMANHO);
                break;
            case 5:
                shellSort(lista, TAMANHO);
                break;
            }
    }while(opt != 0);
    return 0;
}