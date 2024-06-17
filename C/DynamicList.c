#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <locale.h>


typedef struct No{
    int data;
    struct No* next;
}No;

typedef No *ptr_no;
ptr_no list;
int op;

void list_show(ptr_no list){
    // system("cls");
    printf("\nlista: [");
    while(list->next != NULL){
        printf("%d, ", list->data);
        list = list->next;
        }
    printf("%d, ", list->data);
    printf("]");
    }

void list_insert(ptr_no list){
    while(list->next != NULL){
        list = list->next;      
    }
    
    list->next = (ptr_no)malloc(sizeof(No));
    list = list->next;
    list->data = rand()%100;
    list->next = NULL;
}

void list_remove(ptr_no lista){

    ptr_no current;
    current = (ptr_no)malloc(sizeof(No));

    if(list->next != NULL){
        list = list->next;
        current->next = list->next;
    }
}

void menu_show(){
    list_show(list);

    printf("\n\nEscolha uma das opcoes:\n");

    printf("1 - Inserir no final da Lista\n");

    printf("2 - Remover um item da Lista\n");
      
}

void menu_select(int op){
    switch (op)
    {
    case 1:
        list_insert(list);
        break;
    
    case 2:
        list_remove(list);
        break;
    }
}

int main(){
    setlocale(LC_ALL, "Portuguese");

    srand(time(NULL));
    op = 1;
    list = (ptr_no)malloc(sizeof(No));
    list->data = 0;
    list->next = NULL;


    while(op != 0){
        // system("cls");
        menu_show();
        scanf("%d", &op);
        menu_select(op);
    }
    return 0;
}


