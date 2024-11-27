def get_pop_size_at_t(init_pop_size, reprod_rate, time_of_sample):
    calc_size = init_pop_size * (1 + reprod_rate) ** time_of_sample
    return calc_size

initial_population = 10
reproduction_rate = 0.152
times = [10, 50, 100]

for i in times:
    pop_size = get_pop_size_at_t(initial_population, reproduction_rate, i)
    print(f"Expected population size at {i} weeks: {pop_size:.2f}")

