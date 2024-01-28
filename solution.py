"""
D-ary Heap implementation.
@author: Tal Druzhinin & Shelly Goltzman
"""
from common import GeneralAlgorithms
from dheap import DHeap


def extract_max(heap: DHeap):
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
    heap.swap(max_index, heap.heap_size - 1)  # Now max node is at heap[heap.heap_size - 1]
    popped_node = heap.pop_last()
    GeneralAlgorithms.max_heapify(heap, 0)  # Fix Heap from root
    return popped_node


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


def increase_key(heap: DHeap, index_to_increase: int, new_value: int):
    """
    Update the value in index i to k if it's larger than the current value, fix the heap and return the extracted value.

    @param heap: D-ary heap object.
    @param index_to_increase: Requested index to update.
    @param new_value: Value to compare to.
    """
    if heap.heap_size < index_to_increase:
        raise Exception("Heap overflow.")
    if index_to_increase < 0:
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


def extract(heap: DHeap, index_to_remove: int) -> int:
    """
    Extract requested node from heap (assuming heap is a Maximum heap), fix the heap and return the extracted value.

    @param heap: D-ary heap object.
    @param index_to_remove: Requested index to extract from the heap.
    @return: Removed node value.
    """
    if heap.heap_size < index_to_remove:
        raise Exception("Heap overflow.")
    if index_to_remove < 0 or heap.heap_size < 1:
        raise Exception("Heap underflow.")
    heap.swap(index_to_remove, heap.heap_size - 1)  # Now the node to extract is at heap[heap.heap_size - 1]
    popped_node = heap.pop_last()
    # GeneralAlgorithms.build_max_heap(heap)  # Fix Heap
    GeneralAlgorithms.max_heapify(heap, index_to_remove)  # Fix Heap
    return popped_node


# def main():
#     example_array = [3, 9, 2, 11, 14, 5, 7, 15, 6, 10, 20, 12, 1, 17, 4, 13, 16]
#     # example_array = [3]
#     example_heap_level_size = 2
#     example_heap = DHeap(items=example_array, d=example_heap_level_size)
#     print("Height: ", example_heap.height)
#
#     print("Before max_heapify: ")
#     print(example_heap)
#     example_heap.print_as_tree()
#
#     GeneralAlgorithms.build_max_heap(example_heap)
#     print("After max_heapify: ")
#     print(example_heap)
#     example_heap.print_as_tree()
#
#     print("After extract_max: ")
#     max_node = extract_max(example_heap)
#     print(example_heap, "\tMax node value:", max_node)
#     example_heap.print_as_tree()
#
#     print("After insert: ")
#     inserted_value = 9
#     insert(example_heap, inserted_value)
#     print(example_heap, "\tInserted node {}".format(inserted_value))
#     example_heap.print_as_tree()
#
#     print("After pop: ")
#     popped_index = 1
#     popped_node = extract(example_heap, popped_index)
#     print(example_heap, "\tPopped node #{}: {}".format(popped_index, popped_node))
#     example_heap.print_as_tree()
#
#     print("After insert: ")
#     inserted_value = 8
#     insert(example_heap, inserted_value)
#     print(example_heap, "\tInserted node {}".format(inserted_value))
#     example_heap.print_as_tree()
#
#     print("After increase: ")
#     increased_index = example_heap.heap_size - 1
#     increased_value = 16
#     increase_key(example_heap, increased_index, increased_value)
#     print(example_heap, "\tIncreased node #{} to {}:".format(increased_index, increased_value))
#     example_heap.print_as_tree()

# TODO S - User interface -
#           * get D from user (single d for each run)
#           * get heap input from file
#           * allow user to apply all implemented functions or exit, i.e:
#               *  print current state of heap
#               *  ask user which function he would like to run (or exit)
#               *  get function input
#               *  print function output (if any)
#               *  GOTO 1
#           * NOTE: the user can ask to build a new heap from file in the middle of the run
# TODO S+T - analyze runtime complexity of each public function
# TODO S - implement "simple print" (layer 0 - ..., layer 1 - ..., etc) for larger trees


# TODO new-
#  * Check input and throw exceptions on invalid input
#       * Input can be only ints (up to 5k values),
#           positive or *negative*, and can be expected
#           to be between -99999 and 99999
#  * T - Add "Testing" module - i.e. something that gets different inputs and
#       checks if expected output was calculated for each public function
#       also - we have to check for edge cases and raise exceptions in case of an error
#  * Add documentation of the algorithm's basic workflow for each implementation
#  * Validate pseudo code vs final code version
