# Python Data Structures: Stack and Queues

Small, menu-driven Python programs demonstrating core linear data structures.

## Included programs

| File | Concept | Main operations |
| --- | --- | --- |
| `stack.py` | Stack (LIFO) | Push, pop, display |
| `queue.py` | Queue (FIFO) | Enqueue, dequeue, display |
| `circular_queue.py` | Circular queue | Enqueue, dequeue, display |

## Requirements

- Python 3.10 or newer (the current scripts use standard Python features; no third-party packages are required).

## Run

From the repository directory, run one program at a time:

```bash
python stack.py
python queue.py
python circular_queue.py
```

On some systems, use `python3` instead of `python`.

Each program asks for a capacity and then shows an interactive menu. Use the menu's exit option to finish.

## Concepts demonstrated

- **Stack:** last in, first out (LIFO).
- **Queue:** first in, first out (FIFO).
- **Circular queue:** reuses array positions by wrapping the rear index to the beginning.
- **Overflow and underflow:** handles attempts to add to a full structure or remove from an empty one.
- **Input validation:** checks that capacity is a positive integer.

## Complexity

| Operation | Stack | List-backed queue | Circular queue |
| --- | --- | --- | --- |
| Insert | Amortized O(1) | O(1) | O(1) |
| Remove | O(1) | O(n) with `list.pop(0)` | O(1) |
| Display | O(n) | O(n) | O(n) |

The queue implementation uses `list.pop(0)`, which shifts the remaining list elements. For larger workloads, Python's `collections.deque` is a better queue primitive. The circular queue uses a fixed-size list and index arithmetic.

## Learning notes

Try tracing each operation with a small capacity (for example, 3) and write down the contents after every insert/remove. For a circular queue, test the wrap-around case after removing one or more items and inserting again.

## Current limitations and next improvements

- The programs are interactive scripts, so the operations are not yet separated into reusable modules.
- Automated tests are not yet included.
- The circular queue reports overflow/underflow through printed messages rather than return values or exceptions.

Good next steps are to separate each data structure into a class/module, return explicit results for invalid operations, and add unit tests for empty, full, and wrap-around cases.
