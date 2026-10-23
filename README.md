# Python Learning Journey — BSc Computer Science

A structured record of my Python learning during BSc Computer Science: concepts, problem-solving practice, data structures, algorithms, experiments, mistakes, and improvements.

> **Learning-in-progress portfolio.** This repository records practical work and topics explored; it does not claim mastery of every topic listed. Each section should grow with tested code, explanations, and evidence.

## Why this repository exists

I wanted one clear place to show how my Python skills develop over time—not just a collection of files. The goal is to make the learning process visible: what I studied, how I implemented it, what went wrong, and what I improved.

## Learning map

| Stage | Focus | Evidence to add |
|---|---|---|
| 01 | Python foundations | Variables, types, conditions, loops, functions, collections |
| 02 | Problem solving | Small problems, edge cases, readable solutions |
| 03 | Data structures | Stack, queue, circular queue; operations and complexity |
| 04 | Algorithms & complexity | Searching, sorting, Big-O explanations and comparisons |
| 05 | Debugging & testing | Reproducible bugs, fixes, assertions and test cases |
| 06 | Visual programming | Pygame vectors, coordinates, transformations and animation |
| 07 | Mini-projects | Small complete projects with setup and screenshots |
| 08 | Reflection | What became easier, what remains difficult, next goals |

Only mark a topic **Completed** when the code runs and the explanation/tests are present. Otherwise use **In progress** or **Planned**.

## Existing work

- [Stack implementation](stack.py)
- [Queue implementation](queue.py)
- [Circular queue implementation](circular_queue.py)

Related practice includes explaining stack/queue operations, edge cases and time complexity, and Pygame experiments with Vector2 arithmetic, axes, shape drawing, scaling, rotation, positioning and frame timing.

## Repository structure

```text
.
├── README.md
├── stack.py
├── queue.py
├── circular_queue.py
├── algorithms/
│   ├── searching.py
│   └── test_searching.py
├── docs/
│   ├── LEARNING_ROADMAP.md
│   ├── LEARNING_LOG.md
│   ├── PROBLEM_SOLVING_TEMPLATE.md
│   └── PROGRESS.md
├── exercises/
│   ├── basics.py
│   ├── test_basics.py
│   └── README.md
└── pygame-labs/
    ├── vector_lab.py
    └── README.md
```

## Run the new practice examples and tests

Run from the repository root:

```bash
python exercises/basics.py
python algorithms/searching.py
python -m unittest discover -s exercises -p "test_*.py"
python -m unittest discover -s algorithms -p "test_*.py"
```

The Pygame vector lab is a reconstructed learning example. Install its optional dependency before running it:

```bash
python -m pip install pygame
python pygame-labs/vector_lab.py
```

See [the progress snapshot](docs/PROGRESS.md) for details and run instructions.

## How to run the data-structure examples

Install Python 3.10+ and run from the repository root:

```bash
python stack.py
python queue.py
python circular_queue.py
```

If a file uses interactive input, follow its prompts. These commands are suggested entry points; record any adjustments needed for the current version of each script.

## My weekly learning loop

1. Learn one concept.
2. Explain it in my own words.
3. Implement it without copying the final solution.
4. Test normal, boundary and invalid cases.
5. Write down one bug or confusion and how I resolved it.
6. Commit the improvement with a clear message.

## Standards for every future project

- Include a short problem statement and how to run the code.
- Use meaningful names and small functions.
- Test edge cases and state what has not been tested.
- Explain time and space complexity where relevant.
- Never commit passwords, API keys, tokens, database credentials or private data.
- Do not label code production-ready until it has been reviewed and tested.

## Next milestones

- [ ] Review and clean up the current stack, queue and circular queue scripts.
- [ ] Add consistent examples and tests for each operation.
- [x] Add initial searching exercises with complexity notes and unit tests.
- [x] Add a small Pygame vector lab with setup instructions.
- [ ] Add sorting exercises and compare their performance.
- [ ] Review and test every existing data-structure operation.
- [ ] Maintain a dated learning log based on work actually completed.
- [ ] Link finished projects from the profile README.

This repository is a learning record—not a claim that every roadmap item is already complete.
