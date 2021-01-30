elements = [['Li', 'Na', 'K'], ['F', 'Cl', 'Br']]
for inner_list in elements:
    print(inner_list)

# to acces each string in the inner list we can loop over the outer list and then each inner list using nested loop.
el = [['Li', 'Na', 'K'], ['F', 'Cl', 'Br']]
for inner_l in el:
    for item in inner_l:
        print(item)