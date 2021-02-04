# basic operations
dic = {'spam': 2, 'ham': 1, 'egss': 3} # make a dictionary
dic['spam'] # fetch a value by key

len(dic) # number of entries in dic
'ham' in dic # key membership test alternative
list(dic.keys()) # create a new list if dic's keys

# changing dic in place
dic['ham'] = ['girll', 'bake', 'fry'] # change entry(value=list)
del dic['eggs'] #delete entry
dic['brunch'] = 'Bacon' # add new entry

# MORE DIC METHODS
list(dic.values())
list(dic.items())

