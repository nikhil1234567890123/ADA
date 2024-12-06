import matplotlib.pyplot as plt
import networkx as nx
from tabulate import tabulate

def warshall(A, n):
    # Displaying the Cost Adjacency Matrix
    print("Cost Adjacency Matrix:")
    print(tabulate(A, tablefmt='grid'))
    
    # Calculating the Minimum Distance of each node from any other node
    for k in range(n):
        for i in range(n):
            for j in range(n):
                A[i][j] = min(A[i][j], A[i][k] + A[k][j])
    
    # Displaying the resultant Matrix
    print("Shortest Distance of one node from another node\nResultant Matrix:")
    print(tabulate(A, tablefmt='grid'))

def get_user_input():
    # Taking the directed Graph input from the user
    G = nx.DiGraph()
    all_edges = True
    
    while all_edges:
        a = int(input("\nStarting Node of the edge: "))
        b = int(input("Ending Node of the edge: "))
        w = int(input("Enter the cost of the corresponding edge: "))
        G.add_edge(a, b, weight=w)
        ch = input("Do you want to enter another edge? (y/n): ")
        if ch.lower() != 'y':
            all_edges = False
    
    return G

def visualize_graph(G):
    # Displaying/Drawing the Graph
    pos = nx.shell_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color="orange",
            node_size=500, font_size=14, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.35)
    plt.show()

def main():
    print("Warshall's Algorithm")
    G = get_user_input()
    visualize_graph(G)
    
    # Intialising the Cost Adjacency Matrix
    A = nx.to_numpy_array(G)
    n = len(G)
    for i in range(n):
        for j in range(n):
            if i != j and A[i][j] == 0:
                A[i][j] = float('inf')
    
    # Calling the warshall function to find shortest path of each node from any other node
    warshall(A, n)

if __name__ == "__main__":
    main()
