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
    # Check for edge cases
    if heap.heap_size < 1:
        raise Exception("Heap underflow.")
    if heap.heap_size == 1:
        # The only node is the root
        return heap.pop_last()

    # Assuming heap is a max heap - the max node is the root
    max_index = 0

    # Run extract on the max node
    popped_node = extract(heap, max_index)

    return popped_node


def increase_key(heap: DHeap, index_to_increase: int, new_value: int):
    """
    Update the value in index i to k if it's larger than the current value,
    fix the heap and return the extracted value.

    @param heap: D-ary heap object.
    @param index_to_increase: Requested index to update.
    @param new_value: Value to compare to.
    """
    # Check for edge cases
    if heap.heap_size < index_to_increase:
        raise Exception("Heap overflow.")
    if index_to_increase < 0 or heap.heap_size < 1:
        raise Exception("Heap underflow.")

    if heap[index_to_increase] > new_value:
        # The node's value is larger than the new value
        return
    # Node can be increased
    else:
        # Set the node's value to the new value
        heap[index_to_increase] = new_value

        # Fix the heap into a max heap
        while index_to_increase > 0:
            parent_index = heap.get_parent_index(index_to_increase)

            if heap[index_to_increase] > heap[parent_index]:
                # Heap is broken, swap the larger value upwards
                heap.swap(index_to_increase, parent_index)
                index_to_increase = parent_index
            else:
                # Heap is now max heap
                break


def insert(heap: DHeap, value: int):
    """
    Insert requested value into heap (assuming heap is a Maximum heap), and fix the heap.

    @param heap: D-ary heap object.
    @param value: value to insert into the heap.
    """
    # Append Node temporarily to the end of the heap and increase heap_size by one
    heap.insert(heap.heap_size, value)
    heap.heap_size += 1

    # Run increase_key to place the new node in the correct place (fix the heap into a max heap)
    increase_key(heap, heap.heap_size - 1, value)
