import networkx as nx
import matplotlib.pyplot as plt

def greedy_coloring(G, m):
    colors = {}
    for node in G.nodes():
        neighbor_colors = set(colors.get(neighbor, None) for neighbor in G.neighbors(node))
        available_colors = set(range(1, m+1)) - neighbor_colors
        colors[node] = min(available_colors) if available_colors else m + 1
    return colors

G = nx.Graph()
all_edges = True
while all_edges:
    a = int(input("\nStarting Node of the edge: "))
    b = int(input("Ending Node of the edge: "))
    G.add_edge(a, b)
    ch = input("Do you want to enter another edge? (y/n): ")
    if ch.lower() == 'n':
        all_edges = False

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="lightpink", node_size=500, font_size=14, font_weight='bold')
plt.show()

m = int(input("Enter the number of colors: "))
colors = greedy_coloring(G, m)
print("Colors assigned to each vertex:")
for node, color in colors.items():
    print(f"Node {node}: Color {color}")
