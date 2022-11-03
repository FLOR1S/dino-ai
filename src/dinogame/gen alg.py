import numpy
#inputs
equation_inputs = [1, 2.5, -3, 0.23, -4, -1]
#number of weights/inputs
n_weights = 6
#number of solutions per population
n_sol = 8

#shape of population
pop_size = (n_sol, n_weights)

#initial population
new_population = numpy.random.uniform(low=-4.0, high=4.0, size=pop_size)

n_generations = 5

n_parents_mating = 4

for generation in range(n_generations):
    #measuring fitness
    fitness = ga.cal_pop_fitness(equation_inputs,new_population)
    print(str(generation)+" "+fitness)
    #selection
    parents = ga.select_mating_pool (new_population,fitness,n_parents_mating)
    print(str(generation)+" "+parents)
    
    #next gen
    offspring_crossover = ga.crossover(parents,offspring_size(pop_size[0]-parents.shape[0],n_weights))
    print(str(generation)+" "+offspring_crossover)