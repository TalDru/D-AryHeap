"""
This file contains all the functions and algorithms
that are needed for the implementation of the main assignment,
in addition to some auxiliary functions.

@author: Tal Druzhinin & Shelly Goltzman
"""
from dheap import DHeap


class GeneralAlgorithms:

    @classmethod
    def max_heapify(cls, heap: DHeap, root_index: int):
        """
        Heapify given heap from given root index downwards into a Maximum heap
        by swapping the node with the largest value upwards.

        @param heap: D-ary heap object.
        @param root_index: The index of the root node in the subtree to heapify.
        """
        largest_index = root_index
        for child_index in heap.get_children_indexes(root_index):
            if child_index < heap.heap_size and heap[child_index] > heap[largest_index]:
                largest_index = child_index
        if largest_index != root_index:
            heap.swap(root_index, largest_index)
            cls.max_heapify(heap, largest_index)

    @classmethod
    def build_max_heap(cls, heap: DHeap):
        """
        Goes over the heap from the first node with children up to the root and runs heapify on the chosen branch.

        @param heap: D-ary heap object.
        """
        # From the first index with children up to index 0
        for i in reversed(range(0, heap.get_first_leaf_index())):
            cls.max_heapify(heap, i)
