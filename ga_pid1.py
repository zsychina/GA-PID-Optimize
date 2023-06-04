import random
import numpy as np
from pid_fitness import pid1_fitness

POP_SIZE = 5000
NUM_GENERATIONS = 100

K_MAX = 10
K_MIN = 0.001

def fitness(chromosome):
    return pid1_fitness(chromosome[0], chromosome[1], chromosome[2], 2)

# init
pop = []
for i in range(POP_SIZE):
    chromosome = [np.random.uniform(K_MIN, K_MAX) for j in range(3)]
    pop.append(chromosome)
    
# print(pop)

for generation in range(NUM_GENERATIONS):
    fitness_score = [fitness(chromosome) for chromosome in pop]
    
    print('round {}, best score {}'.format(generation, max(fitness_score)))
    
    parents = []
    for i in range(POP_SIZE // 2):
        tournament_size = 50
        contestants = random.sample(range(POP_SIZE), tournament_size)
        winner = max(contestants, key=lambda x: fitness_score[x])
        parents.append(pop[winner])
        contestants.remove(winner)
        loser = max(contestants, key=lambda x: fitness_score[x])
        parents.append(pop[loser])
        
    offspring = []
    for i in range(POP_SIZE):
        parent1, parent2 = random.sample(parents, 2)
        crossover_point = random.randint(1, len(parent1) - 1)
        child = parent1[:crossover_point] + parent2[crossover_point:]
        
        mutation_prob = 0.1
        if random.random() < mutation_prob:
            mutation_point = random.randint(0, len(child) - 1)
            child[mutation_point] = np.random.uniform(K_MIN, K_MAX)
        offspring.append(child)
        
    pop = offspring

best_chromosome = max(pop, key=lambda x: fitness(x))
print("Best parameters:\nKp = {}\nTi = {}\nTd = {}".format(best_chromosome[0],
                                                           best_chromosome[1],
                                                           best_chromosome[2]))
print("Fitness score:", fitness(best_chromosome))



