"""
Given a set of characters and a positive integer k, print all possible strings of length k that can be
formed from the given set.

Input:
set[] = {'a', 'b'}, k = 3

Output:
aaa
aab
aba
abb
baa
bab
bba
bbb


Input:
set[] = {'a', 'b', 'c', 'd'}, k = 1
Output:
a
b
c
d
"""


def generate_all_sets(chars: set, k: int) -> list:
    if k == 0:
        return [""]

    generated_sets = []

    for c in chars:
        for s in generate_all_sets(chars=chars, k=k-1):
            generated_sets.append(c+s)

    return generated_sets


if __name__ == '__main__':
    assert ['aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb'] == generate_all_sets(chars={'a', 'b'}, k=3)
    assert ['a', 'b', 'c', 'd'] == generate_all_sets(chars={'a', 'b', 'c', 'd'}, k=1)

