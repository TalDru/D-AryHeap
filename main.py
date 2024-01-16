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
    heap.swap(0, heap.heap_size - 1)
    # Now max is at heap[heap.heap_size - 1]
    popped_node = heap[heap.heap_size - 1]
    heap.heap_size = heap.heap_size - 1
    GeneralAlgorithms.max_heapify(heap, 0)  # Fix Heap
    return popped_node


def insert(heap: DHeap):
    """
    Insert requested value into heap (assuming heap is a Maximum heap), fix the heap and return the inserted node index.

    @param heap: D-ary heap object.
    @return: Inserted node index.
    """
    
    pass  # TODO Tal


def increase_key(heap: DHeap, i: int, k: int):
    """
    Update the value in index i to k if it's larger than the current value, fix the heap and return the extracted value.

    @param heap: D-ary heap object.
    @param i: Requested index to update.
    @param k: Value to compare to.
    """
    # heap[i] = k if heap[i] < k else heap[i]
    # max_heapify(heap)
    pass  # TODO Shelly


def pop(heap: DHeap, index_to_remove: int):
    """
    Extract requested node from heap (assuming heap is a Maximum heap), fix the heap and return the extracted value.

    @param heap: D-ary heap object.
    @param index_to_remove: Requested index to pop out of the heap.
    @return: Removed node value.
    """
    heap.swap(index_to_remove, heap.heap_size - 1)
    # Now max is at heap[heap.heap_size - 1]
    popped_node = heap[heap.heap_size - 1]
    heap.heap_size = heap.heap_size - 1
    for i in reversed(range(0, heap.heap_size)):
        GeneralAlgorithms.max_heapify(heap, i)  # Fix Heap
    return popped_node


def main():
    example_heap = DHeap([3, 9, 2, 1, 4, 5, 7, 6, 10, 12, 11], 3)
    print("Height: ", example_heap.height)

    print("Before: ")
    print(example_heap)
    example_heap.print_as_tree()

    for i in reversed(range(0, len(example_heap))):
        GeneralAlgorithms.max_heapify(example_heap, i)

    print("After: ")
    print(example_heap)
    example_heap.print_as_tree()

    print("After extract_max: ")
    max_node = extract_max(example_heap)
    print(example_heap, "\tMax node:", max_node)
    example_heap.print_as_tree()

    print("After pop: ")
    popped_index = 2
    popped_node = pop(example_heap, popped_index)
    print(example_heap, "\tPopped node #{}: {}".format(popped_index, popped_node))
    example_heap.print_as_tree()


if __name__ == '__main__':
    main()

# TODO S - User interface -
#           * get D from user
#           * get heap input from file
#           * allow user to apply all implemented functions
# TODO S+T - implement all public functions
# TODO S+T - write down a pseudocode algorythm for each function (including private)
# TODO S+T - analyze runtime complexity of each public function
# TODO S - make printing work better with larger trees
# TODO S - optional - make printing prettier
