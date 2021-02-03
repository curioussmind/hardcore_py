counts = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
print(min(counts)) # print the lowest number from the list

# we can also find the index of the smallest number
low = min(counts)
print(counts.index(low))

#or 
print(counts.index(min(counts)))

# find indices of two smalles values
from typing import List, Tuple

def find_two_smallest(L: List[float]) -> Tuple[int, int]:
    """Return a tuple of the indices of the two smallest values in list L
    >>> items = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    >>> find_two_smallest(items)
    (6, 7)
    >>> items == [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    True
    """
    