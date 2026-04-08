#include <stdio.h>
#include <stdlib.h>

// Structure to represent an edge
typedef struct {
    int u, v, weight;
} Edge;

// Structure to represent a graph
typedef struct {
    int size;
    Edge* edges;
    char** vertex_data;
    int edgeCount;
} Graph;

// Function prototypes
void initGraph(Graph* g, int size);
void addEdge(Graph* g, int u, int v, int weight);
void addVertexData(Graph* g, int vertex, const char* data);
int find(int parent[], int i);
void unionSet(int parent[], int rank[], int x, int y);
void kruskalsAlgorithm(Graph* g);
int compareEdges(const void* a, const void* b);

void initGraph(Graph* g, int size) {
    g->size = size;
    g->edges = (Edge*)malloc(size * size * sizeof(Edge)); // Assuming maximum possible edges
    g->vertex_data = (char**)malloc(size * sizeof(char*));
    g->edgeCount = 0;
}

void addEdge(Graph* g, int u, int v, int weight) {
    g->edges[g->edgeCount].u = u;
    g->edges[g->edgeCount].v = v;
    g->edges[g->edgeCount].weight = weight;
    g->edgeCount++;
}

void addVertexData(Graph* g, int vertex, const char* data) {
    g->vertex_data[vertex] = (char*)malloc(2 * sizeof(char)); // Assuming single character names
    sprintf(g->vertex_data[vertex], "%s", data);
}

int find(int parent[], int i) {
    if (parent[i] == i)
        return i;
    return find(parent, parent[i]);
}

void unionSet(int parent[], int rank[], int x, int y) {
    int xRoot = find(parent, x);
    int yRoot = find(parent, y);

    if (rank[xRoot] < rank[yRoot])
        parent[xRoot] = yRoot;
    else if (rank[xRoot] > rank[yRoot])
        parent[yRoot] = xRoot;
    else {
        parent[yRoot] = xRoot;
        rank[xRoot]++;
    }
}

int compareEdges(const void* a, const void* b) {
    Edge* edgeA = (Edge*)a;
    Edge* edgeB = (Edge*)b;
    return edgeA->weight - edgeB->weight;
}

void kruskalsAlgorithm(Graph* g) {
    Edge result[g->size]; // This will store the resultant MST
    int e = 0; // An index variable, used for result[]
    int i = 0; // An index variable, used for sorted edges

    qsort(g->edges, g->edgeCount, sizeof(g->edges[0]), compareEdges);

    int parent[g->size];
    int rank[g->size];

    for (int node = 0; node < g->size; ++node) {
        parent[node] = node;
        rank[node] = 0;
    }

    while (i < g->edgeCount) {
        Edge next_edge = g->edges[i++];
        int x = find(parent, next_edge.u);
        int y = find(parent, next_edge.v);

        if (x != y) {
            result[e++] = next_edge;
            unionSet(parent, rank, x, y);
        }
    }

    printf("Edge \tWeight\n");
    for (i = 0; i < e; ++i) {
        printf("%s-%s \t%d\n", g->vertex_data[result[i].u], g->vertex_data[result[i].v], result[i].weight);
    }
}

// Main function to demonstrate the Kruskal's Algorithm
int main() {
    Graph g;
    initGraph(&g, 7); // Initialize graph with 7 vertices

    // Add vertex names
    addVertexData(&g, 0, "A");
    addVertexData(&g, 1, "B");
    addVertexData(&g, 2, "C");
    addVertexData(&g, 3, "D");
    addVertexData(&g, 4, "E");
    addVertexData(&g, 5, "F");
    addVertexData(&g, 6, "G");

    // Add edges
    addEdge(&g, 0, 1, 4);  // A-B, weight  4
    addEdge(&g, 0, 6, 10); // A-G, weight 10
    addEdge(&g, 0, 2, 9);  // A-C, weight  9
    addEdge(&g, 1, 2, 8);  // B-C, weight  8
    addEdge(&g, 2, 3, 5);  // C-D, weight  5
    addEdge(&g, 2, 4, 2);  // C-E, weight  2
    addEdge(&g, 2, 6, 7);  // C-G, weight  7
    addEdge(&g, 3, 4, 3);  // D-E, weight  3
    addEdge(&g, 3, 5, 7);  // D-F, weight  7
    addEdge(&g, 4, 6, 6);  // E-G, weight  6
    addEdge(&g, 5, 6, 11); // F-G, weight 11

    printf("Kruskal's Algorithm MST:\n");
    kruskalsAlgorithm(&g);

    return 0;
}

