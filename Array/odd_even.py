"""
The following problem gives good insight into working with arrays: Your input is an array of
integers, and you have to reorder its entries so that the even entries appear first. This is easy if you
use O(n) space, where n is the length of the array. How ever, you are required to solve it without
allocating additional storage.

When working with arrays you should take advantage of the fact that you can operate efficiently
on both ends. For this problem, we can partition the array into three subarrays: Even, Unclassified,
and Odd, appearing in that order. Initially Even and Odd are empty, and Unclassified is the entire
array. We iterate through Unclassified, moving its elements to the boundaries of the Even and Odd
subarrays via swaps, thereby expanding Even and Odd, and shrinking Unclassified.
"""


def even_odd(nums: list):
    left, right = 0, len(nums) - 1

    while left < right:
        if nums[left] % 2 == 0:
            left += 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print('Before: ')
    print(A)

    even_odd(nums=A)

    print('After: ')
    print(A)
