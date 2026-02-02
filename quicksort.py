"""Quicksort implementation with a simple usage example."""

from __future__ import annotations

from typing import Iterable, List, TypeVar

T = TypeVar("T")


def quicksort(values: Iterable[T]) -> List[T]:
    """Return a new list containing the sorted values.

    Args:
        values: Any iterable of orderable items.

    Returns:
        A list containing the items in ascending order.
    """
    items = list(values)
    if len(items) < 2:
        return items

    pivot = items[len(items) // 2]
    less = [item for item in items if item < pivot]
    equal = [item for item in items if item == pivot]
    greater = [item for item in items if item > pivot]
    return quicksort(less) + equal + quicksort(greater)


if __name__ == "__main__":
    sample = [3, 6, 8, 10, 1, 2, 1]
    print("Original:", sample)
    print("Sorted:", quicksort(sample))
