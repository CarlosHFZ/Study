#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAXV 8

typedef struct str_no{
    int id;
    struct str_no *proximo;
} str_no;

struct str_no grafo[MAXV];

void busca_Em_Profundidade(struct str_no g[], int inicio, int alvo){
    int fila[MAXV]; //fila
    bool visitado[MAXV]; //nós visitados
    int indice = 0; //indice do topo da fila
    bool achou = false; //flag de controle (não visitados)
    int corrente = inicio;
    struct str_no *ptr;
    int i;
    printf("=-=-=-= Busca em Largura =-=-=-=\n");
    //Marcando os nós como 'não visitados'.
    for (i = 0; i < MAXV; i++){
        visitado[i]= false;
    }

    //partindo do primeiro vertice.
    printf("VISITANDO: %d\n", corrente);
    visitado[corrente] = true;
    fila[indice] = corrente;
    indice++;

    while(true){
        //Visitar os nós adjacentes ao vértice corrente.
        for (ptr = g[corrente].proximo; ptr != NULL; ptr = ptr->proximo){
            //Caso corrente ainda não tenha sido visitado:
            corrente = ptr->id;
            if(!visitado[corrente]){
                //Enfileira e marca como visitado.
                printf("VISITANDO: %d\n", corrente);
                if (corrente == alvo){
                    printf("Alvo encontrado!\n\n\n");
                    return;
                }
                visitado[corrente] = true;
                fila[indice] = corrente;
                indice++;
            }
        }
        //Caso a fila não esteja vazia:
        if(indice != 0){
            //Atualizando vértice corrente.
            corrente = fila[0];
            //Desenfileirando o priemiro vértice.
            for (i = 1; i < indice + 1; i++){
                fila[i-1] = fila[i];
            }
            indice--;
        }
        else{
            //Não há mais vértices para visitar.
            print("Encerrando busca.\n");
            break;
        }    
    }
    return;
}

void busca_Em_Profundidade(struct str_no g[], int inicio, int alvo){
    int fila[MAXV]; //fila
    bool visitado[MAXV]; //nós visitados
    int indice = 0; //indice do topo da fila
    bool achou = false; //flag de controle (não visitados)
    int corrente = inicio;
    struct str_no *ptr;
    int i;
    printf("=-=-=-= Busca em Profundidade =-=-=-=\n");
    //Marcando os nós como 'não visitados'.
    for (i = 0; i < MAXV; i++){
        visitado[i]= false;
    }
    while(true){
        //Nó corrente não visitado? Marque como visitado.
        //Empilhe o nó corrente.
        if(!visitado[corrente]){
            printf("VISITANDO: %d. \n", corrente);
            if(corrente == alvo){
                printf("Alvo encontrado\n\n\n");
                return;
            }
            visitado[corrente] = true;
            fila[indice] = corrente;
            indice++;
        }
        //Buscando por nós adjacentes, não visitados.
        achou = false;
        for (ptr = g[corrente].proximo; ptr != NULL; ptr = ptr->proximo){
            if(!visitado[ptr->id]){
                achou = true;
                break;
            }
        }
        if(achou){
            //Atualizando o nó corrente.
            corrente = ptr->id;
        }
        else{
            //Não há vertices adjacentes não visitados.
            //Tentando desempilhar o vertice do topo.
            indice--;
            if (indice == -1){
                //Não há mais certices não visitados.
                printf("Encerrando a busca. \n");
                break;
            }
            corrente = fila[indice-1];
        }
    }
    return;
}






//fim
    