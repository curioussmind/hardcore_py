# use multivalued assginment
time, population, growth_rate = 0, 1000, 0.21

# Dont stop until we double the original size
while population != 2000:
    population = population + growth_rate * population
    print(round(population))
    time =+ 1

print("It took", time, "minutes for the bacteria to double.")

