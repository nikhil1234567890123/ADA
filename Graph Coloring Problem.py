import networkx as nx
import matplotlib.pyplot as plt

def nextValue(k, x, A, m):
    while True:
        x[k] = (x[k] + 1) % (m + 1)
        if x[k] == 0:
            return
        j = 0
        while j < len(G):
            if A[k][j] != 0 and x[k] == x[j]:
                break
            j = j + 1
        if j == len(G):
            return

def mcoloring(k, x, A, m):
    while True:
        nextValue(k, x, A, m)
        if x[k] == 0:
            return
        if k == len(G) - 1:
            print(x)
        else:
            mcoloring(k + 1, x, A, m)

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

A = nx.to_numpy_array(G)
x = [0] * (len(G))
m = int(input("Enter the number of colors: "))
print(list(G.nodes()))
print("\nSolutions of the Problem are: ")
mcoloring(0, x, A, m)
