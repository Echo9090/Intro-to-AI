import random

TARGET = 25
POP_SIZE = 6
GENERATIONS = 10

# Create initial population
population = [random.randint(0,50) for _ in range(POP_SIZE)]

def fitness(x):
    return abs(TARGET - x)

for generation in range(GENERATIONS):

    population = sorted(population, key=fitness)

    print("Generation", generation, "Best:", population[0])

    # Select best two parents
    parent1 = population[0]
    parent2 = population[1]

    # Crossover (average)
    child = (parent1 + parent2) // 2

    # Mutation
    child += random.randint(-2,2)

    population[-1] = child

print("Final best solution:", population[0])