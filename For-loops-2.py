
reprod_rate = 0.152
init_pop_size = 0
time_of_sample = [10, 50, 10]

def get_pop_size_at_t(init_pop_size, reprod_rate, time_of_sample):
    pop_growth = []
    for t in time_of_sample:
        growth = init_pop_size, reprod_rate * t
        pop_growth.append(growth)
    return pop_growth

tot = get_pop_size_at_t(init_pop_size, reprod_rate, time_of_sample)

for i in tot:
    print(i)
