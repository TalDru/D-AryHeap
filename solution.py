"""
Implementation of the D-ary Heap algorithms for the assignment.

@author: Tal Druzhinin & Shelly Goltzman
"""
from common import GeneralAlgorithms
from dheap import DHeap


def extract(heap: DHeap, index_to_remove: int) -> int:
    """
    Extract requested node from heap (assuming heap is a Maximum heap), fix the heap and return the extracted value.

    @param heap: D-ary heap object.
    @param index_to_remove: Requested index to extract from the heap.
    @return: Removed node value.
    """
    # Check for edge cases
    if heap.heap_size < index_to_remove:
        raise Exception("Heap overflow.")
    if index_to_remove < 0 or heap.heap_size < 1:
        raise Exception("Heap underflow.")

    # Swap the node to remove with the last node
    heap.swap(index_to_remove, heap.heap_size - 1)

    # Pop the last node (the node to remove)
    popped_node = heap.pop_last()

    # Fix Heap
    GeneralAlgorithms.max_heapify(heap, index_to_remove)

    return popped_node


def extract_max(heap: DHeap) -> int:
    """
    Extract max node assuming heap is a max heap (and therefore the maximum value is at index 0).

    @param heap: D-ary heap object.
    @return: Value of the extracted (largest) node.
    """
    if heap.heap_size < 1:
        raise Exception("Heap underflow.")
    if heap.heap_size == 1:
        # The only node is the root
        return heap.pop_last()
    max_index = 0  # Assuming heap is a max heap
    popped_node = extract(heap, max_index)
    return popped_node


def increase_key(heap: DHeap, index_to_increase: int, new_value: int):
    """
    Update the value in index i to k if it's larger than the current value, fix the heap and return the extracted value.

    @param heap: D-ary heap object.
    @param index_to_increase: Requested index to update.
    @param new_value: Value to compare to.
    """
    if heap.heap_size < index_to_increase:
        raise Exception("Heap overflow.")
    if index_to_increase < 0 or heap.heap_size < 1:
        raise Exception("Heap underflow.")
    if heap[index_to_increase] > new_value:
        return  # New key is smaller than current key
    else:
        heap[index_to_increase] = new_value
        while index_to_increase > 0:
            parent_index = heap.get_parent_index(index_to_increase)
            if heap[index_to_increase] > heap[parent_index]:
                heap.swap(index_to_increase, parent_index)
                index_to_increase = parent_index
            else:
                break


def insert(heap: DHeap, value: int):
    """
    Insert requested value into heap (assuming heap is a Maximum heap), and fix the heap.

    @param heap: D-ary heap object.
    @param value: value to insert into the heap.
    """
    # Append None temporarily to the end of the heap and increase heap_size by one
    heap.insert(heap.heap_size, value)
    heap.heap_size += 1

    increase_key(heap, heap.heap_size - 1, value)

# TODO new-
#  * T - Add documentation of the algorithm's basic workflow for each implementation in the docstring
#  * T - Add more robust commenting, as it was explained in the guide
#  * S+T - Go over inline TODOs
