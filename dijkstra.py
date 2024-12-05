import networkx as nx
import matplotlib.pyplot as plt
from tabulate import tabulate

def shortest_path(graph, source):
    # Initializing the s and dist dictionaries
    s = {v: False for v in graph.nodes()}
    dist = {v: float('inf') for v in graph.nodes()}
    
    # Updating the distance of the neighbours of the source vertex
    for v in graph[source]:
        dist[v] = int(graph[source][v]['weight'])
        s[source] = True
        dist[source] = 0
    
    # Looping through the edges of the graph and updating their distance from the source vertex
    for i in range(1, len(graph)):
        value = float('inf')
        for j in range(1, len(s)):
            if not s[j] and float(value) >= float(dist[j]):
                value = dist[j]
                u = j
                s[u] = True
                for w in graph[u]:
                    if not s[w] and float(dist[w]) > float(dist[u]) + float(graph[u][w]['weight']):
                        dist[w] = int(dist[u]) + int(graph[u][w]['weight'])
    return dist

def main():
    # Taking the Directed Graph from the user as an input
    G = nx.DiGraph()
    all_edges = True
    
    while all_edges:
        a = int(input("\nStarting Node of the edge: "))
        b = int(input("Ending Node of the edge: "))
        w = str(input("Enter the cost of the corresponding edge: "))
        G.add_edge(a, b, weight=w)
        ch = input("Do want to enter another edge? (y/n): ")
        if ch.lower() != 'y':
            all_edges = False
    
    source = int(input("\nEnter the source vertex: "))
    
    # Displaying the graph
    pos = nx.shell_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color="lightpink",
            node_size=500, font_size=14, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()
    
    # Calling the shortestPath function to find shortest path of each vertex from source vertex
    result = shortest_path(G, source)
    
    # Displaying the Resultant table to the user
    table = [[ele, dist] for ele, dist in result.items()]
    print(tabulate(table, headers=["Element", "Distance"], tablefmt='grid'))

if __name__ == "__main__":
    main()
