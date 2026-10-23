"""Small Python practice functions for the BSc learning portfolio.

Run the examples with: python exercises/basics.py
Run tests with: python -m unittest discover -s exercises -p "test_*.py"
"""


def is_even(number: int) -> bool:
    """Return True when number is divisible by two."""
    return number % 2 == 0


def factorial(number: int) -> int:
    """Return number! using iteration; reject negative inputs."""
    if number < 0:
        raise ValueError("factorial is not defined for negative integers")
    result = 1
    for value in range(2, number + 1):
        result *= value
    return result


def count_vowels(text: str) -> int:
    """Count English vowels in text, ignoring letter case."""
    vowels = set("aeiou")
    return sum(1 for character in text.lower() if character in vowels)


def remove_duplicates(items: list) -> list:
    """Keep the first occurrence of each item, preserving input order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def main() -> None:
    print("Python Learning Journey — practice examples")
    print("is_even(12):", is_even(12))
    print("factorial(5):", factorial(5))
    print("count_vowels('Computer Science'):", count_vowels("Computer Science"))
    print("remove_duplicates([3, 1, 3, 2, 1]):", remove_duplicates([3, 1, 3, 2, 1]))


if __name__ == "__main__":
    main()
