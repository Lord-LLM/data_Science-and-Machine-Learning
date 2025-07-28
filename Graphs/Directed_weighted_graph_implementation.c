#include <stdio.h>
#include <stdlib.h>

#define SIZE 4
#define NO_EDGE -1

typedef struct {
    int adjMatrix[SIZE][SIZE];
    char vertexData[SIZE];
} Graph;

void initGraph(Graph *g) {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            g->adjMatrix[i][j] = NO_EDGE;
        }
        g->vertexData[i] = 0;
    }
}

void addEdge(Graph *g, int u, int v, int weight) {
    if (u >= 0 && u < SIZE && v >= 0 && v < SIZE) {
        g->adjMatrix[u][v] = weight;
    }
}

void addVertexData(Graph *g, int vertex, char data) {
    if (vertex >= 0 && vertex < SIZE) {
        g->vertexData[vertex] = data;
    }
}

void printGraph(Graph *g) {
    printf("Adjacency Matrix:\n");
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            if (g->adjMatrix[i][j] == NO_EDGE) {
                printf("0 ");
            } else {
                printf("%d ", g->adjMatrix[i][j]);
            }
        }
        printf("\n");
    }
    printf("\nVertex Data:\n");
    for (int i = 0; i < SIZE; i++) {
        printf("Vertex %d: %c\n", i, g->vertexData[i]);
    }
}

int main() {
    Graph g;
    initGraph(&g);

    addVertexData(&g, 0, 'A');
    addVertexData(&g, 1, 'B');
    addVertexData(&g, 2, 'C');
    addVertexData(&g, 3, 'D');
    addEdge(&g, 0, 1, 3); // A -> B with weight 3
    addEdge(&g, 0, 2, 2); // A -> C with weight 2
    addEdge(&g, 3, 0, 4); // D -> A with weight 4
    addEdge(&g, 2, 1, 1); // C -> B with weight 1

    printGraph(&g);

    return 0;
}

