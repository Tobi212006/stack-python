"""Searching algorithms with clear contracts and complexity notes."""


def linear_search(values: list[int], target: int) -> int:
    """Return the first matching index, or -1 if target is absent.

    Time: O(n) worst case. Extra space: O(1).
    """
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1


def binary_search(sorted_values: list[int], target: int) -> int:
    """Find target in an ascending-sorted list; return index or -1.

    The input must already be sorted in ascending order.
    Time: O(log n). Extra space: O(1).
    """
    left, right = 0, len(sorted_values) - 1
    while left <= right:
        middle = (left + right) // 2
        current = sorted_values[middle]
        if current == target:
            return middle
        if current < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1


if __name__ == "__main__":
    numbers = [2, 5, 8, 12, 16, 23, 38]
    print("Linear search for 12:", linear_search(numbers, 12))
    print("Binary search for 23:", binary_search(numbers, 23))
    print("Binary search for 7:", binary_search(numbers, 7))
