import matplotlib.pyplot as plt
import networkx as nx

def multistage_graph(graph, k, n):
    cost = [0] * n
    d = [0] * n
    path = [0] * (k - 1)
    cost[n - 1] = 0.0

    for j in range(n - 2, -1, -1):
        minimum = float('inf')
        for r in range(j + 1, n):
            if graph[j][r] != 0 and graph[j][r] + cost[r] < minimum:
                minimum = graph[j][r] + cost[r]
                d[j] = r + 1
        cost[j] = minimum
        d[n - 1] = n

    path[0] = 1
    path[k - 2] = n

    for j in range(1, k - 1):
        path[j] = d[path[j - 1]]
    path.insert(1, d[0])

    return cost[0], path

def get_user_input():
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

    k = int(input("\nEnter the number of stages in the graph: "))
    return G, k

def visualize_graph(G):
    pos = nx.shell_layout(G)  # Use shell layout instead of spring layout
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color="lightpink",
            node_size=500, font_size=14, font_weight='bold', arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()

def visualize_path(G, result):
    pos = nx.shell_layout(G)  # Use shell layout instead of spring layout
    edge_labels = nx.get_edge_attributes(G, 'weight')
    
    edge_colors = ['red' if (u, v) in zip(result[1], result[1][1:]) else 'black' for u, v in G.edges()]
    edge_widths = [4 if (u, v) in zip(result[1], result[1][1:]) else 1 for u, v in G.edges()]

    nx.draw(G, pos, with_labels=True, node_color="lightpink",
            node_size=500, font_size=14, font_weight='bold', arrows=True)
    nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=edge_widths, arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()

def main():
    print("Multistage Graph Problem")
    G, k = get_user_input()
    visualize_graph(G)

    A = nx.to_numpy_array(G)
    result = multistage_graph(A, k, len(G))

    print("\nMinimum cost to go from source to sink is:", result[0])
    visualize_path(G, result)

if __name__ == "__main__":
    main()
