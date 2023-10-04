import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt
import time


# Create a random graph (you can replace this with your own graph)
def create_random_graph(num_nodes, probability):
    G = nx.erdos_renyi_graph(num_nodes, probability)
    return G


# Initialize pheromone levels on edges
def initialize_pheromones(graph, num_colors):
    pheromones = {}
    for node in graph.nodes():
        for color in range(num_colors):
            pheromones[(node, color)] = random.uniform(0.1, 1.0)
    return pheromones


# Ant Colony Optimization algorithm
def aco(graph, num_ants, num_iterations, evaporation_rate, alpha, beta, num_colors):
    best_coloring = None
    best_solution = float('inf')

    start_time = time.time()

    for iteration in range(num_iterations):
        pheromones = initialize_pheromones(graph, num_colors)
        for ant in range(num_ants):
            coloring = {}
            for node in graph.nodes():
                available_colors = set(range(num_colors))
                for neighbor in graph.neighbors(node):
                    if neighbor in coloring:
                        available_colors.discard(coloring[neighbor])

                if not available_colors:
                    # All colors are used by neighbors, pick a random color
                    color = random.randint(0, num_colors - 1)
                else:
                    # Choose a color using ACO probabilities
                    probabilities = []
                    for color in available_colors:
                        pheromone = pheromones[(node, color)]
                        heuristic = len(available_colors)  # Simple heuristic
                        probabilities.append((color, pheromone ** alpha * heuristic ** beta))

                    probabilities = [(color, prob / sum([p[1] for p in probabilities])) for color, prob in
                                     probabilities]
                    chosen_color = np.random.choice([color for color, _ in probabilities],
                                                    p=[prob for _, prob in probabilities])
                    color = chosen_color

                coloring[node] = color

            # Calculate the number of conflicts in the coloring
            conflicts = sum(1 for u, v in graph.edges() if coloring[u] == coloring[v])

            if conflicts < best_solution:
                best_coloring = coloring
                best_solution = conflicts

            # Update pheromone levels based on the ant's solution
            for edge in graph.edges():
                u, v = edge
                if coloring[u] == coloring[v]:
                    pheromones[(u, coloring[u])] = (1 - evaporation_rate) * pheromones[(u, coloring[u])] + 1.0

        # Evaporate pheromone levels
        for node in graph.nodes():
            for color in range(num_colors):
                pheromones[(node, color)] = (1 - evaporation_rate) * pheromones[(node, color)]

    end_time = time.time()

    execution_time = end_time - start_time

    return best_solution, best_coloring, execution_time


if __name__ == "__main__":
    num_nodes = 20
    probability = 0.3
    num_ants = 10
    num_iterations = 50
    evaporation_rate = 0.1
    alpha = 1.0
    beta = 2.0
    num_colors = 4  # You can set the number of colors here.

    G = create_random_graph(num_nodes, probability)
    best_solution, best_coloring, execution_time = aco(G, num_ants, num_iterations, evaporation_rate, alpha, beta,
                                                       num_colors)

    print("Призначені кольори:", best_coloring)
    print("Вартість розфарбування:", best_solution)
    print("Час виконання:", execution_time, "сек.")

    # Draw the graph with colors
    pos = nx.spring_layout(G, seed=42)
    colors = [best_coloring[node] for node in G.nodes()]
    nx.draw(G, pos, node_color=colors, cmap=plt.get_cmap("viridis"), with_labels=True)
    plt.show()