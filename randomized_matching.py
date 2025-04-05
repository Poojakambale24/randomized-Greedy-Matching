import random
import time
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v):
        self.edges.append((u, v))

    def randomized_greedy_matching(self):
        """ Randomized Greedy Algorithm for Maximum Matching """
        random.shuffle(self.edges)
        matched = set()
        matching = []

        for u, v in self.edges:
            if u not in matched and v not in matched:
                matching.append((u, v))
                matched.add(u)
                matched.add(v)

        return matching

    def standard_greedy_matching(self):
        """ Standard Greedy Algorithm """
        matched = set()
        matching = []

        for u, v in sorted(self.edges):  # Sort edges to make it deterministic
            if u not in matched and v not in matched:
                matching.append((u, v))
                matched.add(u)
                matched.add(v)

        return matching

# Generate a random graph
def generate_graph(num_nodes, num_edges):
    graph = Graph(num_nodes)
    edges = set()
    while len(edges) < num_edges:
        u, v = random.sample(range(num_nodes), 2)
        if (u, v) not in edges and (v, u) not in edges:
            edges.add((u, v))
            graph.add_edge(u, v)
    return graph

# Performance Testing
num_nodes = 100
num_edges = 250
graph = generate_graph(num_nodes, num_edges)

start = time.time()
rand_matching = graph.randomized_greedy_matching()
rand_time = time.time() - start

start = time.time()
greedy_matching = graph.standard_greedy_matching()
greedy_time = time.time() - start

print(f"Randomized Greedy Matching Size: {len(rand_matching)}, Time: {rand_time:.5f} sec")
print(f"Standard Greedy Matching Size: {len(greedy_matching)}, Time: {greedy_time:.5f} sec")

# Visualization
labels = ['Randomized Greedy', 'Standard Greedy']
sizes = [len(rand_matching), len(greedy_matching)]
times = [rand_time, greedy_time]

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.bar(labels, sizes, color=['blue', 'green'])
plt.ylabel('Matching Size')
plt.title('Comparison of Matching Sizes')

plt.subplot(1, 2, 2)
plt.bar(labels, times, color=['red', 'orange'])
plt.ylabel('Execution Time (seconds)')
plt.title('Comparison of Execution Times')

plt.show()
