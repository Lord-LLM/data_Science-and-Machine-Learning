// Traverse linked lists to find the smallest element
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

int findLowestValue(struct Node* head) {
    int minValue = head->data;
    struct Node* currentNode = head->next;
    while (currentNode) {
        if (currentNode->data < minValue) {
            minValue = currentNode->data;
        }
        currentNode = currentNode->next;
    }
    return minValue;
}

int main() {
    struct Node* node1 = (struct Node*) malloc(sizeof(struct Node));
    struct Node* node2 = (struct Node*) malloc(sizeof(struct Node));
    struct Node* node3 = (struct Node*) malloc(sizeof(struct Node));
    struct Node* node4 = (struct Node*) malloc(sizeof(struct Node));
    struct Node* node5 = (struct Node*) malloc(sizeof(struct Node));

    node1->data = 7;
    node2->data = 11;
    node3->data = 3;
    node4->data = 2;
    node5->data = 9;

    node1->next = node2;
    node2->next = node3;
    node3->next = node4;
    node4->next = node5;
    node5->next = NULL;

    printf("The lowest value in the linked list is: %d\n", findLowestValue(node1));

    return 0;
}

//C