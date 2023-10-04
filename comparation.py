import matplotlib.pyplot as plt
from main import mmas
from aco import aco
import networkx as nx


def create_random_graph(num_nodes, probability):
    G = nx.erdos_renyi_graph(num_nodes, probability)
    return G


num_nodes = 10
probability = 0.5
graph = create_random_graph(num_nodes, probability)
m = 4
max_iterations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
rho = 0.1
alpha = 0.5
beta = 0.5
max_tau = 10.0
min_tau = 0.001
num_ants = 100

mmas_time = []
mmas_cost = []
aco_time = []
aco_cost = []

for i in max_iterations:
    # Запускаємо MMAS
    best_solution_mmas, _, execution_time_mmas = mmas(graph, m, num_ants, i, rho, alpha, beta, max_tau, min_tau)
    mmas_cost.append(best_solution_mmas)
    mmas_time.append(execution_time_mmas)

    # Запускаємо ACO
    best_solution_aco, _, execution_time_aco = aco(graph, num_ants, i, rho, alpha, beta, m)
    aco_cost.append(best_solution_aco)
    aco_time.append(execution_time_aco)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(max_iterations, mmas_cost, marker='o', label='MMAS')
plt.plot(max_iterations, aco_cost, marker='x', label='ACO')
plt.xlabel('Ітерації')
plt.ylabel('Вартість')
plt.title('Збіжність (Вартість)')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(max_iterations, mmas_time, marker='o', label='MMAS')
plt.plot(max_iterations, aco_time, marker='x', label='ACO')
plt.xlabel('Ітерації')
plt.ylabel('Час (секунди)')
plt.title('Збіжність (Час)')
plt.legend()

plt.tight_layout()
plt.show()
