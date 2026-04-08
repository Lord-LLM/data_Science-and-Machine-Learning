#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

void traverseAndPrint(Node* head) {
    Node* currentNode = head;
    while (currentNode != NULL) {
        printf("%d -> ", currentNode->data);
        currentNode = currentNode->next;
    }
    printf("null\n");
}

Node* insertNodeAtPosition(Node* head, Node* newNode, int position) {
    if (position == 1) {
        newNode->next = head;
        return newNode;
    }

    Node* currentNode = head;
    for (int i = 1; i < position - 1 && currentNode != NULL; i++) {
        currentNode = currentNode->next;
    }

    if (currentNode != NULL) {
        newNode->next = currentNode->next;
        currentNode->next = newNode;
    }
    return head;
}

int main() {
    Node* node1 = malloc(sizeof(Node));
    node1->data = 7;
    
    Node* node2 = malloc(sizeof(Node));
    node2->data = 3;
    
    Node* node3 = malloc(sizeof(Node));
    node3->data = 2;
    
    Node* node4 = malloc(sizeof(Node));
    node4->data = 9;

    node1->next = node2;
    node2->next = node3;
    node3->next = node4;

    printf("Original list:\n");
    traverseAndPrint(node1);

    // Insert a new node with value 97 at position 2
    Node* newNode = malloc(sizeof(Node));
    newNode->data = 97;
    node1 = insertNodeAtPosition(node1, newNode, 2);

    printf("\nAfter insertion:\n");
    traverseAndPrint(node1);

    free(node1);
    free(node2);
    free(node3);
    free(node4);
    free(newNode);

    return 0;
}

//C