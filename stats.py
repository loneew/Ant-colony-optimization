from main import mmas
import matplotlib.pyplot as plt
import networkx as nx


def create_random_graph(num_nodes, probability):
    G = nx.erdos_renyi_graph(num_nodes, probability)
    return G


# Функція для відображення графа
def plot_graph(G):
    pos = nx.spring_layout(G, seed=42)
    colors = [best_coloring[node] for node in G.nodes()]
    nx.draw(G, pos, node_color=colors, cmap=plt.get_cmap("viridis"), with_labels=True)
    plt.show()


# Приклад використання
num_nodes = 10  # Кількість вершин
probability = 0.5  # Ймовірність створення зв'язків
graph = create_random_graph(num_nodes, probability)
m = 4
max_iterations = 10
rho = 0.1
alpha = 0.5
beta = 0.5
max_tau = 10.0
min_tau = 0.001
num_ants = 100  # Кількість мурах (фіксований параметр)

best_solution, best_coloring, execution_time = mmas(graph, m, num_ants, max_iterations, rho, alpha, beta, max_tau,
                                                    min_tau)

print("Призначені кольори:", best_coloring)
print("Вартість розфарбування:", best_solution)
print("Час виконання:", execution_time, "сек.")
plot_graph(graph)

# Дослідження впливу параметра m (кількість кольорів)
m_values = list(range(1, 4))  # Діапазон значень m
execution_times_m = []  # Час виконання для кожного значення m
best_solutions_m = []  # Вартість розфарбування для кожного значення m

for m_value in m_values:
    # Запускаємо алгоритм та зберігаємо результати
    best_solution, _, execution_time = mmas(graph, m_value, num_ants, max_iterations, rho, alpha, beta, max_tau,
                                            min_tau)
    execution_times_m.append(execution_time)
    best_solutions_m.append(best_solution)

# Графік залежності часу виконання від кількості кольорів (m)
plt.figure(figsize=(8, 6))
plt.subplot(1, 2, 1)

plt.plot(m_values, execution_times_m, marker='o')
plt.title('Залежність часу виконання від кількості кольорів')
plt.xlabel('Кількість кольорів (m)')
plt.ylabel('Час виконання (сек)')
plt.grid(True)

# Графік залежності вартості розфарбування від кількості кольорів (m)
plt.subplot(1, 2, 2)
plt.plot(m_values, best_solutions_m, marker='o')
plt.title('Залежність вартості розфарбування від кількості кольорів')
plt.xlabel('Кількість кольорів (m)')
plt.ylabel('Вартість розфарбування')
plt.grid(True)
plt.show()

# Дослідження впливу параметра max_iterations (максимальна кількість ітерацій)
max_iterations_values = list(range(5, 101, 5))  # Діапазон значень max_iterations
execution_times_iterations = []  # Час виконання для кожного значення max_iterations
best_solutions_iterations = []  # Вартість розфарбування для кожного значення max_iterations

for max_iter in max_iterations_values:
    # Запускаємо алгоритм та зберігаємо результати
    best_solution, _, execution_time = mmas(graph, m, num_ants, max_iter, rho, alpha, beta, max_tau, min_tau)
    execution_times_iterations.append(execution_time)
    best_solutions_iterations.append(best_solution)

# Графік залежності часу виконання від max_iterations (максимальна кількість ітерацій)
plt.figure(figsize=(8, 6))
plt.subplot(1, 2, 1)
plt.plot(max_iterations_values, execution_times_iterations, marker='o')
plt.title('Залежність часу виконання від максимальної кількості ітерацій')
plt.xlabel('Максимальна кількість ітерацій (max_iterations)')
plt.ylabel('Час виконання (сек)')
plt.grid(True)

# Графік залежності вартості розфарбування від max_iterations (максимальна кількість ітерацій)
plt.subplot(1, 2, 2)
plt.plot(max_iterations_values, best_solutions_iterations, marker='o')
plt.title('Залежність вартості розфарбування від максимальної кількості ітерацій')
plt.xlabel('Максимальна кількість ітерацій (max_iterations)')
plt.ylabel('Вартість розфарбування')
plt.grid(True)
plt.show()

# Дослідження впливу параметра rho (коефіцієнт випаровування феромону)
rho_values = [0.01, 0.1, 0.3, 0.5, 0.7, 0.9]  # Діапазон значень rho
execution_times_rho = []  # Час виконання для кожного значення rho
best_solutions_rho = []  # Вартість розфарбування для кожного значення rho

for rho_value in rho_values:
    # Запускаємо алгоритм та зберігаємо результати
    best_solution, _, execution_time = mmas(graph, m, num_ants, max_iterations, rho_value, alpha, beta, max_tau,
                                            min_tau)
    execution_times_rho.append(execution_time)
    best_solutions_rho.append(best_solution)

# Графік залежності часу виконання від rho (коефіцієнт випаровування феромону)
plt.figure(figsize=(8, 6))
plt.subplot(1, 2, 1)
plt.plot(rho_values, execution_times_rho, marker='o')
plt.title('Залежність часу виконання від коефіцієнта випаровування феромону')
plt.xlabel('Коефіцієнт випаровування феромону (rho)')
plt.ylabel('Час виконання (сек)')
plt.grid(True)

# Графік залежності вартості розфарбування від rho (коефіцієнт випаровування феромону)
plt.subplot(1, 2, 2)
plt.plot(rho_values, best_solutions_rho, marker='o')
plt.title('Залежність вартості розфарбування від коефіцієнта випаровування феромону')
plt.xlabel('Коефіцієнт випаровування феромону (rho)')
plt.ylabel('Вартість розфарбування')
plt.grid(True)
plt.show()

# Дослідження впливу параметра alpha (вага феромону)
alpha_values = [0.1, 0.3, 0.5, 0.7, 0.9]  # Діапазон значень alpha
execution_times_alpha = []  # Час виконання для кожного значення alpha
best_solutions_alpha = []  # Вартість розфарбування для кожного значення alpha

for alpha_value in alpha_values:
    # Запускаємо алгоритм та зберігаємо результати
    best_solution, _, execution_time = mmas(graph, m, num_ants, max_iterations, rho, alpha_value, beta, max_tau,
                                            min_tau)
    execution_times_alpha.append(execution_time)
    best_solutions_alpha.append(best_solution)

# Графік залежності часу виконання від alpha (вага феромону)
plt.figure(figsize=(8, 6))
plt.subplot(1, 2, 1)
plt.plot(alpha_values, execution_times_alpha, marker='o')
plt.title('Залежність часу виконання від ваги феромону (alpha)')
plt.xlabel('Вага феромону (alpha)')
plt.ylabel('Час виконання (сек)')
plt.grid(True)

# Графік залежності вартості розфарбування від alpha (вага феромону)
plt.subplot(1, 2, 2)
plt.plot(alpha_values, best_solutions_alpha, marker='o')
plt.title('Залежність вартості розфарбування від ваги феромону (alpha)')
plt.xlabel('Вага феромону (alpha)')
plt.ylabel('Вартість розфарбування')
plt.grid(True)
plt.show()

# Дослідження впливу параметра beta (вага доступних кольорів)
beta_values = [0.1, 0.3, 0.5, 0.7, 0.9]  # Діапазон значень beta
execution_times_beta = []  # Час виконання для кожного значення beta
best_solutions_beta = []  # Вартість розфарбування для кожного значення beta

for beta_value in beta_values:
    # Запускаємо алгоритм та зберігаємо результати
    best_solution, _, execution_time = mmas(graph, m, num_ants, max_iterations, rho, alpha, beta_value, max_tau,
                                            min_tau)
    execution_times_beta.append(execution_time)
    best_solutions_beta.append(best_solution)

# Графік залежності часу виконання від beta (вага доступних кольорів)
plt.figure(figsize=(8, 6))
plt.subplot(1, 2, 1)
plt.plot(beta_values, execution_times_beta, marker='o')
plt.title('Залежність часу виконання від ваги доступних кольорів (beta)')
plt.xlabel('Вага доступних кольорів (beta)')
plt.ylabel('Час виконання (сек)')
plt.grid(True)

# Графік залежності вартості розфарбування від beta (вага доступних кольорів)
plt.subplot(1, 2, 2)
plt.plot(beta_values, best_solutions_beta, marker='o')
plt.title('Залежність вартості розфарбування від ваги доступних кольорів (beta)')
plt.xlabel('Вага доступних кольорів (beta)')
plt.ylabel('Вартість розфарбування')
plt.grid(True)
plt.show()

# Дослідження впливу параметра max_tau (максимальний рівень феромону)
max_tau_values = [1.0, 10.0, 100.0]  # Діапазон значень max_tau
execution_times_max_tau = []  # Час виконання для кожного значення max_tau
best_solutions_max_tau = []  # Вартість розфарбування для кожного значення max_tau

for max_tau_value in max_tau_values:
    # Запускаємо алгоритм та зберігаємо результати
    best_solution, _, execution_time = mmas(graph, m, num_ants, max_iterations, rho, alpha, beta, max_tau_value,
                                            min_tau)
    execution_times_max_tau.append(execution_time)
    best_solutions_max_tau.append(best_solution)

# Графік залежності часу виконання від max_tau (максимальний рівень феромону)
plt.figure(figsize=(8, 6))
plt.subplot(1, 2, 1)
plt.plot(max_tau_values, execution_times_max_tau, marker='o')
plt.title('Залежність часу виконання від максимального рівня феромону (max_tau)')
plt.xlabel('Максимальний рівень феромону (max_tau)')
plt.ylabel('Час виконання (сек)')
plt.grid(True)

# Графік залежності вартості розфарбування від max_tau (максимальний рівень феромону)
plt.subplot(1, 2, 2)
plt.plot(max_tau_values, best_solutions_max_tau, marker='o')
plt.title('Залежність вартості розфарбування від максимального рівня феромону (max_tau)')
plt.xlabel('Максимальний рівень феромону (max_tau)')
plt.ylabel('Вартість розфарбування')
plt.grid(True)
plt.show()

# Дослідження впливу параметра min_tau (мінімальний рівень феромону)
min_tau_values = [0.001, 0.01, 0.1, 1.0]  # Діапазон значень min_tau
execution_times_min_tau = []  # Час виконання для кожного значення min_tau
best_solutions_min_tau = []  # Вартість розфарбування для кожного значення min_tau

for min_tau_value in min_tau_values:
    # Запускаємо алгоритм та зберігаємо результати
    best_solution, _, execution_time = mmas(graph, m, num_ants, max_iterations, rho, alpha, beta, max_tau,
                                            min_tau_value)
    execution_times_min_tau.append(execution_time)
    best_solutions_min_tau.append(best_solution)

# Графік залежності часу виконання від min_tau (мінімальний рівень феромону)
plt.figure(figsize=(8, 6))
plt.subplot(1, 2, 1)
plt.plot(min_tau_values, best_solutions_min_tau, marker='o')
plt.title('Залежність часу виконання від мінімального рівня феромону (min_tau)')
plt.xlabel('Мінімальний рівень феромону (min_tau)')
plt.ylabel('Час виконання (сек)')
plt.grid(True)

# Графік залежності вартості розфарбування від min_tau (мінімальний рівень феромону)
plt.subplot(1, 2, 2)
plt.plot(min_tau_values, best_solutions_min_tau, marker='o')
plt.title('Залежність вартості розфарбування від мінімального рівня феромону (min_tau)')
plt.xlabel('Мінімальний рівень феромону (min_tau)')
plt.ylabel('Вартість розфарбування')
plt.grid(True)
plt.show()
