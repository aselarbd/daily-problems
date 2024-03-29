"""
Given a number n, find all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.
Examples:


Input:  N = 2
Output:
0101 1111 1001 0110 0000 1010

Input:  N = 3
Output:
011011 001001 011101 010001 101011 111111
110011 101101 100001 110101 001010 011110
010010 001100 000000 010100 101110 100010
110110 100100
"""


def find_all_binary_sequences_with_same_sum(n: int) -> list:

    result = []

    def find_all_binary_sequences(length: int) -> list:
        if length == 0:
            return ['']

        combinations = []
        for i in find_all_binary_sequences(length=length-1):
            combinations.append('0'+i)
            combinations.append('1'+i)
        return combinations

    all_seq = find_all_binary_sequences(length=2*n)

    for seq in all_seq:
        if seq[:n].count('1') == seq[n:].count('1'):
            result.append(seq)

    return result


if __name__ == '__main__':
    result = find_all_binary_sequences_with_same_sum(n=2)
    print(result)
