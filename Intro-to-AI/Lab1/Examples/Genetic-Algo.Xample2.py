import random

TARGET = "10110"
POP_SIZE = 6
GENERATIONS = 10

# Create initial population
population = [
    ''.join(random.choice('01') for _ in range(len(TARGET)))
    for _ in range(POP_SIZE)
]

def fitness(individual):
    score = 0
    for i in range(len(TARGET)):
        if individual[i] == TARGET[i]:
            score += 1
    return score

for generation in range(GENERATIONS):

    population = sorted(population, key=fitness, reverse=True)

    print("Generation", generation, "Best:", population[0], "Fitness:", fitness(population[0]))

    parent1 = population[0]
    parent2 = population[1]

    # Crossover
    point = random.randint(1, len(TARGET)-1)
    child = parent1[:point] + parent2[point:]

    # Mutation
    child = list(child)
    index = random.randint(0, len(TARGET)-1)
    child[index] = random.choice('01')
    child = ''.join(child)

    population[-1] = child

print("\nFinal best solution:", population[0])