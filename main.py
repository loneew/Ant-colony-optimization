import random
import time


def mmas(graph, m, num_ants, max_iterations, rho, alpha, beta, max_tau, min_tau):
    V = len(graph.nodes())  # Отримуємо кількість вершин у графі
    best_solution = float('inf')  # Найкраще знайдене рішення
    best_coloring = None  # Найкраще розфарбування
    pheromone = [[1.0] * V for _ in range(V)]  # Матриця феромону на ребрах графа

    start_time = time.time()  # Запускаємо лічильник часу

    for iteration in range(max_iterations):
        for ant in range(num_ants):
            color = [-1] * V  # Список кольорів для вершин
            uncolored_vertices = list(graph.nodes())  # Список нерозфарбованих вершин

            while uncolored_vertices:
                v = random.choice(uncolored_vertices)  # Вибираємо вершину для розфарбування
                available_colors = list(range(1, m + 1))  # Доступні кольори для вершини

                for neighbor in graph.neighbors(v):
                    if color[neighbor] in available_colors:
                        available_colors.remove(color[neighbor])

                if not available_colors:
                    available_colors = list(
                        range(1, m + 1))  # Якщо всі кольори вже використані, дозволяємо вибрати будь-який

                prob = [0.0] * m

                # Обчислюємо ймовірності для кольорів на основі феромону та обмежень
                for c in available_colors:
                    prob[c - 1] = (pheromone[v][c - 1] ** alpha) * ((1.0 / len(available_colors)) ** beta)

                # Обчислюємо кумулятивні ймовірності
                cum_prob = [sum(prob[:i + 1]) for i in range(len(prob))]

                # Вибираємо кольори на основі кумулятивних ймовірностей
                rand_val = random.uniform(0, cum_prob[-1])
                for c, cp in enumerate(cum_prob):
                    if rand_val <= cp:
                        selected_color = c + 1
                        break

                color[v] = selected_color
                uncolored_vertices.remove(v)

            cost = sum([1 for u, v in graph.edges() if color[u] == color[v]])  # Розрахунок вартості розфарбування

            if len(set(color)) == m:  # Перевіряємо, чи розфарбування коректне
                if cost < best_solution:
                    best_solution = cost
                    best_coloring = color[:]

                    # Оновлюємо рівні феромону на ребрах для рішення
                    for u, v in graph.edges():
                        if color[u] == color[v]:  # Зменшуємо феромон для конфліктних вершин
                            pheromone[u][v] = (1 - rho) * pheromone[u][v]
                        else:  # Збільшуємо феромон для неконфліктних вершин
                            if cost == 0:
                                pheromone[u][v] = (1 - rho) * pheromone[u][v] + 1.0  # Збільшуємо феромон на 1.0
                            else:
                                pheromone[u][v] = (1 - rho) * pheromone[u][v] + (1.0 / cost)

        # Оновлюємо глобальні рівні феромону
        for u, v in graph.edges():
            pheromone[u][v] = max(min_tau, min(max_tau, (1 - rho) * pheromone[u][v]))

    end_time = time.time()  # Зупиняємо лічильник часу

    # Визначаємо час виконання
    execution_time = end_time - start_time

    return best_solution, best_coloring, execution_time
