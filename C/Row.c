#include <stdio.h>
#include <stdlib.h>
#include <locale.h>


//constant
#define SIZE 5

//creatin the queue structure
struct Size_queue{
    
    int data[SIZE];
    int start;
    int end;
};

//declaring the queue variable
struct Size_queue queue;
int op;



//functio that show the content from de queue
void queue_mostrar(){

    int i;
    printf("[");

    for (i = 0; i < SIZE; i++){
        printf("%d,", queue.data[i]);
    }
    printf("]\n\n");
}

//add an element to the end of the queue
void queue_enter(){

    if (queue.end == SIZE){
        system("cls");
        printf("\nThe queue is full, impossible to add a new value\n\n");    
    }
    else{
        system("cls");     
        printf("\nEnter the value to be entered: ");
        
        scanf("%d", &queue.data[queue.end]);
        queue.end++;
        system("cls"); 
        
        
    }
    queue_mostrar();
}

//remove the first element from the queue
void queue_leave(){

    if (queue.start == queue.end){
        system("cls");
        printf("\nThe queue is empty, there is nothing to remove!\n\n");

    }
    else{
        system("cls");
        int i;

        for (i = 0; i < SIZE; i++){
            queue.data[i] = queue.data[i+1];
        }

        queue.data[queue.end] = 0;
        queue.end--;
    }
    queue_mostrar();
}



void menu_mostrar(){
    printf("Oque Deseja fazer?\n\n"
    "Case 1: Adcionar um elemento a pilha.\n"
    "Case 2: Remover o ultimo elemento da pilha\n\n"
    "Ou digite 0 para sair!\n\n");
}

int main(int argc, char const *argv[])
{
    setlocale(LC_ALL, "Portuguese");
    op = 1;

    queue.start = 0;
    queue.end = 0;

    while (op != 0){
        menu_mostrar();
        scanf("%d", &op);

        switch (op)
        {
        case 1:
            queue_enter();
            break;
        
        case 2:
            queue_leave();
            break;
        }


    }


    return 0;
}
