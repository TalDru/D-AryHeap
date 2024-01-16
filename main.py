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
    max_index = 0  # Assuming heap is a max heap
    heap.swap(max_index, heap.heap_size - 1)  # Now max node is at heap[heap.heap_size - 1]
    popped_node = heap.pop_last()
    GeneralAlgorithms.max_heapify(heap, 0)  # Fix Heap from root
    return popped_node


def insert(heap: DHeap):
    """
    Insert requested value into heap (assuming heap is a Maximum heap), fix the heap and return the inserted node index.

    @param heap: D-ary heap object.
    @return: Inserted node index.
    """

    pass  # TODO Shelly


def increase_key(heap: DHeap, i: int, k: int):
    """
    Update the value in index i to k if it's larger than the current value, fix the heap and return the extracted value.

    @param heap: D-ary heap object.
    @param i: Requested index to update.
    @param k: Value to compare to.
    """
    if heap[i] >= k:
        return
    else:
        heap[i] = k
        while i > 0:
            parent_index = heap.get_parent_index(i)
            if heap[i] > heap[parent_index]:
                heap.swap(i, parent_index)
                i = parent_index
            else:
                break


def pop(heap: DHeap, index_to_remove: int):
    """
    Extract requested node from heap (assuming heap is a Maximum heap), fix the heap and return the extracted value.

    @param heap: D-ary heap object.
    @param index_to_remove: Requested index to pop out of the heap.
    @return: Removed node value.
    """
    heap.swap(index_to_remove, heap.heap_size - 1)  # Now the node to extract is at heap[heap.heap_size - 1]
    popped_node = heap.pop_last()
    GeneralAlgorithms.build_max_heap(heap)  # Fix Heap
    return popped_node


def main():
    example_array = [3, 9, 2, 11, 14, 5, 7, 15, 6, 10, 20, 12, 1, 17, 4, 13, 16]
    example_heap_level_size = 3
    example_heap = DHeap(items=example_array, d=example_heap_level_size)
    print("Height: ", example_heap.height)

    print("Before max_heapify: ")
    print(example_heap)
    example_heap.print_as_tree()

    GeneralAlgorithms.build_max_heap(example_heap)
    print("After max_heapify: ")
    print(example_heap)
    example_heap.print_as_tree()

    print("After extract_max: ")
    max_node = extract_max(example_heap)
    print(example_heap, "\tMax node value:", max_node)
    example_heap.print_as_tree()

    print("After pop: ")
    popped_index = 1
    popped_node = pop(example_heap, popped_index)
    print(example_heap, "\tPopped node #{}: {}".format(popped_index, popped_node))
    example_heap.print_as_tree()

    print("After increase: ")
    increased_index = example_heap.heap_size - 1
    increased_value = 16
    increase_key(example_heap, increased_index, increased_value)
    print(example_heap, "\tIncreased node #{} to {}:".format(increased_index, increased_value))
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
