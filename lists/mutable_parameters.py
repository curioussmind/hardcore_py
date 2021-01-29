def remove_last_item(L: list) -> list:
    """Return last L with the last item removed

    precondition: len(L) => 0

    >>> remove_last_item([1, 2, 3, 4])
    [1, 2, 3]
    """
    del L[-1]
    return L
L = input([])
print(L)