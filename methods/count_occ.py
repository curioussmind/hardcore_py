def count_occ(s1: str, s2: str, ch: str) -> int:
    return s1.count(ch) + s2.count(ch)

print(count_occ('misro', 'dardi', 'r'))
print(count_occ('red', 'blue', 'l'))
print(count_occ('green', 'purple', 'b'))

