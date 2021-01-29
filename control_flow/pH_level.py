def ph_level(ph: int) -> str:
    if ph <= 4:
         return 'strong acid!'
    elif ph <= 6:
        return 'weak acid'
    elif ph == 7:
        return 'neutral'
    elif ph <= 9:
        return 'Weak base'
    elif ph <= 14:
        return 'Strong base'

ph = input('Enter the pH value: ')
ph = int(ph)
print(f'The pH level of {ph} is {ph_level(ph)}!')
