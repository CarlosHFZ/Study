#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

#define TAMANHO 10

int lista[TAMANHO];
int lista_Desordenada[TAMANHO];
int opt = -1;
int qtd = 0;
int changes = 0;
int comp = 0;


void lista_mostrar(void){
    printf("Lista Ordenada: [");
    for (int i = 0; i < TAMANHO; i++){
        printf("%d, ", lista[i]);
    }
    printf("]\n");
}

void menu_mostrar(void){
    printf("\n\n");
    printf("Tempo = %d iteracoes", qtd);
    printf("\nComparacoes: %d\nTrocas: %d\n\n", comp, changes);
    printf("1 - Gerar lista aleatoriamente\n");
    printf("2 - Criar lista manualmente\n");
    printf("3 - Ordenar com BubbleSort\n");
    printf("4 - Ordenar com SelectSort\n");
    printf("5 - Ordenar com insertionSort\n");
    printf("6 - Ordenar com ShellSort\n");
    printf("9 - Utilizar lista atual\n");
    printf("0 - Sair...\n\n");
}

void lista_gerar(void){
    for (int i = 0; i < TAMANHO; i++){
        lista_Desordenada[i] = rand()%50;
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
        lista[i] = lista_Desordenada[i];
    }
}

void lista_mostrar_ordenado(void){
    printf("Lista Desordenada: [");
    for (int i = 0; i < TAMANHO; i++){       
        printf("%d, ", lista_Desordenada[i]);
    }
    printf("]");
}

void troca(int* a, int* b){
    int tmp;
    tmp = *a;
    *a = *b;
    *b = tmp;
    changes++;
    qtd++;
}

void zerar(void){
    qtd = 0;
    comp = 0;
    changes = 0;   
}

//////ORDENAÇÃO POR BUBBLESORT (MÉTODO DA BOLHA)
int bubbleSort(int vec[]){
    int qtd, i, j, tmp;

    for (i = 0; i < TAMANHO; i++){
        for (j = i+1; j < TAMANHO; j++){
            if (vec[i] > vec[j]){
                comp++;
                qtd++;
                troca(&vec[i], &vec[j]);
            }
            qtd++;
            comp++;
        }
    }
    return(qtd);
}

//////ORDENAÇÃO POR SELECTIONSORT
int selectionSort(int vec[], int tam){
    int i, j, min;

    for (i = 0; i <(tam-1); i++){
        min = i;
        for(j = (i+1); j < tam; j++){
            
            if (vec[j] < vec[min]){
                min = j;
                comp++;
                qtd++;
            }
            comp++;
            qtd++;
        }
        if (i != min){
            troca(&vec[i], &vec[min]);
            comp++;
            qtd++;
        }
    }
    return(qtd);
}

/////ORDENAÇÃO POR INSERTIONSORT
int insertionSort(int vec[], int tam){
    int i, j;
    for (i = 1; i < tam; i++){
        j = i;       
        while(vec[j] < vec[j-1] && j != 0){
            troca(&vec[j], &vec[j-1]);
            j--;
            qtd++;
            comp++;
        }
        comp++;     
    }
    return(qtd);
}

/////ORDENAÇÃO POR SHELLSORT UNIASSELVI
int shellSortUnia(int vec[], int tam){
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

/////ORDENAÇÃO POR SHELLSORT PONTO ACADÊMICO
void shellSortPA(int vec[], int tam){
    int i, j, aux;
    qtd++;
    float k = log(TAMANHO+1)/log(3);
    qtd++;
    k = floor(k+0.5);
    qtd++;
    int h = (pow(3, k)-1)/2;
    qtd++;
    while(h > 0){
        for (i = 0; i < TAMANHO-h; i++){
            qtd++;
            comp++;
            if (lista[i] > lista[i+h]){
                aux = lista[i+h];
                lista[i+h] = lista[i];
                lista[i] = aux;
                j = i-h;
                changes++;
                qtd++;
                while(j>=0){
                    comp++;
                    qtd++;
                    if(aux<lista[j]){
                        lista[j+h] = lista[j];
                        lista[j] = aux;
                        changes++; 
                        qtd++;
                    } else {break;}
                    j = j-h;
                    qtd++;
                }
            }
        } h = (h-1)/3; 
        qtd++;
    }
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
                zerar();
                lista_gerar();
                lista_limpar();
                break;
                
            case 2:
                zerar();
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
                insertionSort(lista, TAMANHO);
                break;
            case 6:
                shellSortPA(lista, TAMANHO);              
                break;
            case 9:
                lista_limpar();
                zerar();             
                break;
            }
    }while(opt != 0);
    return 0;
}