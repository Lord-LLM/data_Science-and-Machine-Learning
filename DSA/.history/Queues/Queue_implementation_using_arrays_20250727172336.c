#include <stdio.h>
#include <stdbool.h>
#include <string.h>

#define MAX 100   // Max queue size

char queue[MAX];  // Queue array
int front = 0;    // Index of front element
int rear = -1;    // Index of last element

// Enqueue operation
void enqueue(char element) {
    if (rear < MAX - 1) {
        queue[++rear] = element;
    } else {
        printf("Queue Overflow!\n");
    }
}

// Dequeue operation
char dequeue() {
    if (front <= rear) {
        return queue[front++];
    } else {
        printf("Queue Underflow!\n");
        return '\0';  // Return null character on underflow
    }
}

// Peek operation
char peek() {
    if (front <= rear) {
        return queue[front];
    } else {
        printf("Queue is empty!\n");
        return '\0';
    }
}

// isEmpty
bool isEmpty() {
    return front > rear;
}

// Size
int size() {
    return rear - front + 1;
}

// Print queue
void printQueue() {
    printf("Queue: ");
    for (int i = front; i <= rear; i++) {
        printf("%c ", queue[i]);
    }
    printf("\n");
}

int main() {
    enqueue('A');
    enqueue('B');
    enqueue('C');
    printQueue();

    char removed = dequeue();
    printf("Dequeue: %c\n", removed);

    char frontElem = peek();
    printf("Peek: %c\n", frontElem);

    printf("isEmpty: %s\n", isEmpty() ? "true" : "false");
    printf("Size: %d\n", size());

    return 0;
}
