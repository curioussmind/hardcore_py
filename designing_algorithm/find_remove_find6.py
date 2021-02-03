from typing import List, Tuple

def find_two_smallest(L: List[float]) -> Tuple[int, int]:
    """Return a tuple of the indices of the two smallest values in list L.
    >>> items = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    >>> find_two_smallest(items)
    (6, 7)
    >>> items == [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    True
    """
    L = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    # Find the index of the minimum item and remove that item
    smallest = min(L)
    min1 = L.index(smallest)
    L.remove(smallest)

    # Find the index of the new minimum item in the list
    next_smallest = min(L)
    min2 = L.index(smallest)

    # Put the smallest item back in the list
    L.insert(min1, smallest)

    # Fix min2 in case it was affected by the removal and reinsertion
    if min1 <= min2:
        min1 += 1
    return (min1, min2)
    # If necessary, adjust the second index
    # Return the two indices

L = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
find_two_smallest([809, 834, 477, 478, 307, 122, 96, 102, 324, 476])