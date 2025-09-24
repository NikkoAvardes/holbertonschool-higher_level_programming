#!/usr/bin/env python3
"""CountedIterator - Keeping Track of Iteration"""


class CountedIterator:
    """Iterator that counts iterations."""

    def __init__(self, data):
        self.iterator = iter(data)
        self.count = 0

    def __next__(self):
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Return current count."""
        return self.count

    def __iter__(self):
        return self
