with open('planet.txt', 'r') as planets_file:
    planets = planets_file.readlines()

print(planets)
for planet in sorted(planets):
    print(planet.strip())
