with open('planet.txt', 'r') as data_file:
    for line in data_file:
        print(len(line.strip()))