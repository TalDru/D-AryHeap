import pytest

from common import GeneralAlgorithms
from dheap import DHeap
from solution import extract_max, extract, increase_key, insert


def make_heap(items, d, maximize=True, heap_size=None):
    h = DHeap(items, d)

    if maximize:
        GeneralAlgorithms.build_max_heap(h)

    if heap_size is not None:
        h.heap_size = heap_size

    return h


@pytest.mark.parametrize(
    "heap,expected_heap,expected_result",
    [
        (
                make_heap([1, -30, 5, 15, 21, 7], 2),
                make_heap([15, 5, 7, 1, -30, 21], 2, maximize=False, heap_size=5),
                21
        ),
        (
                make_heap([1], 2),
                make_heap([1], 2, maximize=False, heap_size=0),
                1
        ),
        (
                make_heap([-10, -20, -40, -30, -20], 3),
                make_heap([-20, -20, -40, -30, -10], 3, maximize=False, heap_size=4),
                -10
        )
    ]
)
#
def test_extract_max(heap: DHeap, expected_heap: DHeap, expected_result: int):
    max_node = extract_max(heap)

    assert max_node == expected_result
    assert heap == expected_heap
    assert heap.heap_size == expected_heap.heap_size


@pytest.mark.parametrize(
    "heap,expected_heap,remove_index,expected_result",
    [
        (
                make_heap([1, -30, 5, 15, 21, 7], 2),
                make_heap([21, 5, 7, 1, -30, 15], 2, maximize=False, heap_size=5),
                1,
                15
        ),
        (
                make_heap([1], 2),
                make_heap([1], 2, maximize=False, heap_size=0),
                0,
                1
        ),
    ]
)
#
def test_extract(heap: DHeap, expected_heap: DHeap, remove_index: int, expected_result: int):
    removed_node = extract(heap, remove_index)

    assert removed_node == expected_result
    assert heap == expected_heap
    assert heap.heap_size == expected_heap.heap_size


@pytest.mark.parametrize(
    "heap,expected_heap,insert_value",
    [
        (
                make_heap([5, 10, -4, 20, 3, 1, 1], 3),
                make_heap([21, 10, 20, 5, 3, 1, 1, -4], 3, maximize=False),
                21,
        ),
        (
                make_heap([1, 2, 3, 4], 2),
                make_heap([4, 3, 3, 1, 2], 2, maximize=False),
                3,
        ),
        (
                make_heap([1, 2, 3, 4], 2),
                make_heap([4, 2, 3, 1, 1], 2, maximize=False),
                1,
        ),
    ]
)
#
def test_insert(heap: DHeap, expected_heap: DHeap, insert_value: int):
    insert(heap, insert_value)

    assert heap == expected_heap
    assert heap.heap_size == expected_heap.heap_size


@pytest.mark.parametrize(
    "heap,expected_heap,increase_index,increase_value",
    [
        (
                make_heap([5, 10, -4, 20, 3, 1, 1], 3),
                make_heap([20, 12, -4, 5, 3, 1, 1], 3, maximize=False),
                1,
                12
        ),
        (
                make_heap([5, 4, 3, -1, 3, 2], 2),
                make_heap([5, 4, 3, -1, 3, 2], 2, maximize=False),
                0,
                4
        ),
        (
                make_heap([5, 4, 3, -1, 3, 2], 2),
                make_heap([20, 5, 3, -1, 4, 2], 2, maximize=False),
                4,
                20
        ),
    ]
)
def test_increase_key(heap: DHeap, expected_heap: DHeap, increase_index: int, increase_value: int):
    increase_key(heap, increase_index, increase_value)

    assert heap == expected_heap
    assert heap.heap_size == expected_heap.heap_size


@pytest.mark.parametrize(
    "heap,actions,kwargs,expected_results,expected_heaps",
    [
        (
                make_heap([3, 9, 2, 11, 14, 5, 7, 15, -200, 6, 10, 20, 12, 1, -17, 4, 14, 16], 4),
                [extract_max, insert, extract, insert, increase_key, increase_key],
                [
                    {},
                    {"value": 0},
                    {"index_to_remove": 1},
                    {"value": 2},
                    {"index_to_increase": 3, "new_value": 15},
                    {"index_to_increase": 0, "new_value": 10}
                ],
                [20, None, 15, None, None, None],
                [
                    make_heap(
                        [16, 15, 12, 14, 14, 5, 7, 9, -200, 6, 10, 2, 3, 1, -17, 4, 11, 20],
                        4,
                        maximize=False,
                        heap_size=17
                    ),
                    make_heap(
                        [16, 15, 12, 14, 14, 5, 7, 9, -200, 6, 10, 2, 3, 1, -17, 4, 11, 0, 20],
                        4,
                        maximize=False,
                        heap_size=18
                    ),
                    make_heap(
                        [16, 9, 12, 14, 14, 5, 7, 0, -200, 6, 10, 2, 3, 1, -17, 4, 11, 15, 20],
                        4,
                        maximize=False,
                        heap_size=17
                    ),
                    make_heap(
                        [16, 9, 12, 14, 14, 5, 7, 0, -200, 6, 10, 2, 3, 1, -17, 4, 11, 2, 15, 20],
                        4,
                        maximize=False,
                        heap_size=18
                    ),
                    make_heap(
                        [16, 9, 12, 15, 14, 5, 7, 0, -200, 6, 10, 2, 3, 1, -17, 4, 11, 2, 15, 20],
                        4,
                        maximize=False,
                        heap_size=18
                    ),
                    make_heap(
                        [16, 9, 12, 15, 14, 5, 7, 0, -200, 6, 10, 2, 3, 1, -17, 4, 11, 2, 15, 20],
                        4,
                        maximize=False,
                        heap_size=18
                    ),
                ]
        ),
    ]
)
def test_sequence(heap: DHeap, actions: list, kwargs: list, expected_results: list, expected_heaps: list):
    for i in range(0, len(actions)):
        action = actions[i]
        args = kwargs[i]
        result = action(heap, **args)

        assert result == expected_results[i]
        assert heap == expected_heaps[i]
        assert heap.heap_size == expected_heaps[i].heap_size
