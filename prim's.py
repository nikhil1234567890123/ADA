import sys
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def min_key(self, key, mst_set):
        min_val = sys.maxsize
        min_index = None

        for v in range(self.V):
            if key[v] < min_val and not mst_set[v]:
                min_val = key[v]
                min_index = v

        return min_index

    def prim_mst(self, start_node):
        parent = [-1] * self.V
        key = [sys.maxsize] * self.V
        mst_set = [False] * self.V

        key[start_node - 1] = 0
        parent[start_node - 1] = -1

        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not mst_set[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        mst_edges = []
        for i in range(self.V):
            if parent[i] != -1:
                mst_edges.append((parent[i] + 1, i + 1, self.graph[i][parent[i]]))

        return mst_edges

def main():
    vertices = int(input("Enter the number of vertices: "))
    graph = Graph(vertices)

    while True:
        start = int(input("Enter the starting node of the edge (1-based index): "))
        end = int(input("Enter the ending node of the edge (1-based index): "))
        weight = int(input("Enter the weight of the edge: "))

        graph.graph[start - 1][end - 1] = weight
        graph.graph[end - 1][start - 1] = weight

        choice = input("Do you want to enter another edge? (yes/no): ")
        if choice.lower() != "yes":
            break

    start_node = int(input("Enter the starting node for MST (1-based index): "))

    mst_edges = graph.prim_mst(start_node)

    # Create NetworkX graph from adjacency matrix
    G = nx.Graph()
    for i in range(vertices):
        for j in range(vertices):
            if graph.graph[i][j] > 0:
                G.add_edge(i + 1, j + 1, weight=graph.graph[i][j])

    # Plot the original graph
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title('Original Graph')
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=12, font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Construct MST graph
    mst_graph = nx.Graph()
    for edge in mst_edges:
        mst_graph.add_edge(edge[0], edge[1], weight=edge[2])

    # Plot the MST
    plt.subplot(1, 2, 2)
    plt.title('Minimum Spanning Tree (MST)')
    pos_mst = nx.spring_layout(G)  # Use the same layout as the original graph
    nx.draw(mst_graph, pos, with_labels=True, node_size=700, node_color='lightgreen', font_size=12, font_weight='bold')
    edge_labels_mst = nx.get_edge_attributes(mst_graph, 'weight')
    nx.draw_networkx_edge_labels(mst_graph, pos, edge_labels=edge_labels_mst)

    # Display the plots
    plt.show()

    return mst_edges

if __name__ == "__main__":
    mst_edges = main()
    print("Edges in the Minimum Spanning Tree (MST):")
    for edge in mst_edges:
        print(f"{edge[0]} - {edge[1]} (Weight: {edge[2]})")
