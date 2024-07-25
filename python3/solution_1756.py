"""
# Prompt

Design and implement a HitCounter class that keeps track of requests (or hits). It should support 
the following operations:

    `record(timestamp)`: records a hit that happened at timestamp
    `total()`: returns the total number of hits recorded
    `range(lower, upper)`: returns the number of hits that occurred between timestamps lower and 
      upper (inclusive)

# Followup

What if our system has limited memory?

# Notes

## Initial solution

* We can record timestamps in any order
* Need an efficient way to query for a range of elements
* Could store elements in a balanced binary tree and make sure that sums are percolated upwards for
  fast queries

## Followup

If we have limited memory we would realistically want to turn to a database in real life, but
for the sake of this problem we could go a couple of ways. We could chunk by time buckets, or we could
chunk by some number of records to a disk.

If we chose time buckets, we would have to specify a bucket size. Then we could have separate files
that correspond to some bucket window (much like a database), and each file could store the granular
time points. To get even fancier, you could store metadata at the beginning of the file so that you
can also easily get the number of instances in an entire bucket if you're querying for a span that
goes beyond an individual bucket.

For example, if you have a bucket size of 1ms, and you have two files that correspond to 1-2 ms and 2-3 ms,
and the user queries for the number of hits between 0 and 2.5 ms, you can just get the total number of hits
in the 1-2ms bucket, and then query the 2-3 ms bucket with more granularity.
"""

import bisect
from dataclasses import dataclass


@dataclass
class Node:
    """
    A node in a tree for tracking hits.
    """

    timestamp: int
    """The timestamp the hit corresponds to."""

    count: int
    """The number of hits that correspond to the timestamp."""

    descendant_conut: int
    # TODO: not sure if we want to maintain this, is it really worth it over a traversal?
    """The number of descendants under this node, exluding itself."""


class BTree[T]:
    """A binary node."""

    def __init__(self):
        self.root = None
        """
        The root node.

        Initially set to `None` if the binary tree isn't initialized.
        """


class HitCounter:
    """Keeps track of requests/hits and allows for basic queries in a time span."""

    def __init__(self) -> None:
        self.recorded_timestamps: list[int] = list()
        """All of the timestamps that have been recorded so far."""

    def record(self, timestamp: int) -> None:
        """
        Record a hit that happened at `timestamp`.

        Args:
            timestamp: A unix timestamp. This must be a non-negative integer.
        """
        if timestamp < 0:
            raise ValueError("Unix epoch timestamp must not be negative.")
        insertion_idx = bisect.bisect_left(self.recorded_timestamps, timestamp)
        # Technically can be $O(n)$ if Python has to shuffle the entire list.
        self.recorded_timestamps.insert(insertion_idx, timestamp)

    @property
    def total(self) -> int:
        """The total number of hits recorded."""
        return len(self.recorded_timestamps)

    def range(self, lower_bound: int, upper_bound: int) -> int:
        """
        Return the total number of hits that happened in some range.

        Args:
            lower_bound: The lower bound to get the hits for, inclusive. This must be less than
              or equal to `upper_bound`.
            upper_bound: The upper bound to get the hits for, inclusive. This must be greater than
              or equal to `lower_bound`.
        """
        if lower_bound > upper_bound:
            raise ValueError(
                "The lower bound must be less than or equal to the upper bound"
            )
        lower_idx = bisect.bisect_left(self.recorded_timestamps, lower_bound)
        upper_idx = bisect.bisect_right(self.recorded_timestamps, upper_bound)
        return upper_idx - lower_idx

    def __len__(self) -> int:
        return self.total
