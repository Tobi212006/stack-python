"""Unit tests for the reusable data structures."""
import unittest
from data_structures import CircularQueue, Queue, Stack

class StackTests(unittest.TestCase):
    def test_lifo_and_peek(self):
        s = Stack(2); s.push("A"); s.push("B")
        self.assertEqual(s.peek(), "B")
        self.assertEqual([s.pop(), s.pop()], ["B", "A"])
        self.assertTrue(s.is_empty())
    def test_overflow_underflow_and_capacity(self):
        s = Stack(1); s.push(1)
        with self.assertRaises(OverflowError): s.push(2)
        s.pop()
        with self.assertRaises(IndexError): s.pop()
        with self.assertRaises(ValueError): Stack(0)

class QueueTests(unittest.TestCase):
    def test_fifo_and_peek(self):
        q = Queue(2); q.enqueue("A"); q.enqueue("B")
        self.assertEqual(q.peek(), "A")
        self.assertEqual([q.dequeue(), q.dequeue()], ["A", "B"])
    def test_overflow_underflow(self):
        q = Queue(1); q.enqueue(1)
        with self.assertRaises(OverflowError): q.enqueue(2)
        q.dequeue()
        with self.assertRaises(IndexError): q.dequeue()

class CircularQueueTests(unittest.TestCase):
    def test_wraparound(self):
        q = CircularQueue(3)
        for value in ("A", "B", "C"): q.enqueue(value)
        self.assertEqual(q.dequeue(), "A")
        q.enqueue("D")
        self.assertEqual([q.dequeue(), q.dequeue(), q.dequeue()], ["B", "C", "D"])
        self.assertTrue(q.is_empty())
    def test_bounds(self):
        q = CircularQueue(1)
        with self.assertRaises(IndexError): q.dequeue()
        q.enqueue("A")
        with self.assertRaises(OverflowError): q.enqueue("B")
        self.assertEqual(q.dequeue(), "A")
        with self.assertRaises(ValueError): CircularQueue(0)

if __name__ == "__main__":
    unittest.main()
