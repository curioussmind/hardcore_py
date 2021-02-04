table = {'1975': 'Holly Grail',
        '1979': 'Life of Brian',
        '1983': 'The Meaning of Life'}

year = '1983'
movie = table[year] # dictionary[key] => value
print(movie)

for year in table:
    print(year + '\t' + table[year])
    
