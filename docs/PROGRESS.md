# Learning Portfolio — Progress Snapshot

This page records what is currently present in the repository, not a claim that every topic in the roadmap has been mastered.

## Added in this milestone

- Beginner practice functions: even/odd, factorial, vowel counting, ordered duplicate removal.
- Unit tests for those functions using Python's built-in `unittest`.
- Linear search and binary search examples, with complexity notes and tests.
- A Pygame vector lab demonstrating Vector2 arithmetic and mapping Cartesian coordinates to screen coordinates.
- Existing stack, queue, and circular queue work remains part of the portfolio.

## Run the standard-library tests

Run each test file from the repository root:

```bash
python -m unittest discover -s exercises -p "test_*.py"
python -m unittest discover -s algorithms -p "test_*.py"
```

The two commands use separate discovery roots because each test folder imports its neighbouring module directly.

## Run examples

```bash
python exercises/basics.py
python algorithms/searching.py
```

For the vector lab, install Pygame first:

```bash
python -m pip install pygame
python pygame-labs/vector_lab.py
```

## Accuracy note

The vector lab is a clean reconstruction based on previously discussed Pygame practice. It is not represented as the exact original classroom source file. The roadmap should be updated only after the learner can explain the code and has run the examples locally.
