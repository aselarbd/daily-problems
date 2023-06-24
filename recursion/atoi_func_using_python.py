"""
The atoi() function takes a string (which represents an integer) as an argument and returns its value.
We have discussed iterative implementation of atoi(). How to compute recursively?
"""


def atoi(num: str) -> int:
    if len(num) == 0:
        return 0

    return (int(num[0]) * (10 ** len(num[1:]))) + atoi(num=num[1:])


if __name__ == '__main__':
    assert atoi(num='123456') == 123456
    assert atoi(num='456334') == 456334
    assert atoi(num='000304') == 304
    assert atoi(num='0000500') == 500
