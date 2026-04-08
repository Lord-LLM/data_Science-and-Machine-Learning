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

Node* deleteSpecificNode(Node* head, Node* nodeToDelete) {
    if (head == nodeToDelete) {
        Node* newHead = head->next;
        free(head);
        return newHead;
    }

    Node* currentNode = head;
    while (currentNode->next && currentNode->next != nodeToDelete) {
        currentNode = currentNode->next;
    }

    if (currentNode->next == NULL) {
        return head;
    }

    Node* temp = currentNode->next;
    currentNode->next = currentNode->next->next;
    free(temp);

    return head;
}

int main() {
    Node* node1 = malloc(sizeof(Node));
    node1->data = 7;
    Node* node2 = malloc(sizeof(Node));
    node2->data = 11;
    Node* node3 = malloc(sizeof(Node));
    node3->data = 3;
    Node* node4 = malloc(sizeof(Node));
    node4->data = 2;
    Node* node5 = malloc(sizeof(Node));
    node5->data = 9;

    node1->next = node2;
    node2->next = node3;
    node3->next = node4;
    node4->next = node5;

    printf("Before deletion:\n");
    traverseAndPrint(node1);

    node1 = deleteSpecificNode(node1, node4);

    printf("\nAfter deletion:\n");
    traverseAndPrint(node1);

    free(node1);
    free(node2);
    free(node3);
    free(node5);

    return 0;
}

