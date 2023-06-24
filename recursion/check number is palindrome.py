"""
Given a positive integer, write a function that returns true if the given number is a palindrome, else false.
For example, 12321 is a palindrome, but 1451 is not a palindrome.
"""


def is_palindrome(num: str) -> bool:
    if len(num) == 0:
        return True
    if num[0] != num[-1]:
        return False
    return is_palindrome(num=num[1:-1])


if __name__ == '__main__':
    assert is_palindrome(num='2002')
    assert is_palindrome(num='2033302')
    assert is_palindrome(num='203454302')
    assert not is_palindrome(num='2044544402')
