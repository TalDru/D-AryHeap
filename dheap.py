"""
This file contains the implementation of a DAry Heap object as a type of array,
including common internal actions and calculations preformed on heaps.
The class also includes the visualization modules for printing the object.

@author: Tal Druzhinin & Shelly Goltzman
"""

import math

MAX_NODE_VALUE_LENGTH = 6


class DHeap(list):
    """
    Implementation of a D-ary Heap object as a type of array.
    """

    # Class definitions
    def __init__(self, items, d):
        super().__init__()

        # Validate input
        if d < 2:
            raise Exception("Heap was initiated with a level size smaller than 2!")
        if len(items) < 1:
            raise Exception("Heap was initiated with an invalid list of values!")

        # Populate heap object
        self.d = d
        self.heap_size = 0
        for item in items:
            self.heap_size += 1
            self.append(item)

    def __setitem__(self, key, value):
        list.__setitem__(self, key, value)

    # Properties

    @property
    def height(self) -> int:
        """
        Calculate the height of the current heap.

        @return: The height of the heap.
        """
        return int(math.floor(math.log(self.heap_size, self.d))) + 1 if self.heap_size > 0 else 0

    # Class functionality

    def swap(self, i: int, j: int):
        """
        Swap values of the node in index i with the value of the node index j.

        @param i: First index.
        @param j: Second index.
        """
        self[i], self[j] = self[j], self[i]

    def pop_last(self) -> int:
        """
        Pop the last node of the heap by decreasing the heap_size counter.

        @return: The popped node's value
        """
        last_index = self.heap_size - 1
        popped_node = self[last_index]
        self.heap_size -= 1
        return popped_node

    # Class calculations

    def get_parent_index(self, root_index: int) -> int:
        """
        Calculate the theoretical index of the parent of a given index.
        @note: This is a mathematical calculation that does not validate the heap boundaries.


        @param root_index: The index to find the parent of.
        @return: The parent index of the given root index.
        """
        return int(math.floor((root_index - 1) / self.d))

    def nth_child_index(self, root_index: int, n: int) -> int:
        """
        Calculate the theoretical index of the n-th child of a given index.
        @note: This is a mathematical calculation that does not validate the heap boundaries.

        @param root_index: The index to find the child of.
        @param n: The cardinal number of the child (e.g. 1st, 2nd, etc.).
        @return: The child index of the given root index.
        """
        return (self.d * root_index) + n

    def get_children_indexes(self, root_index: int) -> list:
        """
        Calculate the theoretical indexes of all the child of a given index.
        @note: This is a mathematical calculation that does not validate the heap boundaries.

        @param root_index: The index to find the child of.
        @return: A list of all potential child indexes of the given root index.
        """
        return [self.nth_child_index(root_index, n) for n in range(1, self.d + 1)]

    def get_first_leaf_index(self):
        """
        Calculate the index of the first childless node ("leaf") of the heap.

        @return: The index of the first leaf in the heap.
        """
        return int(math.floor(self.heap_size + 1 / self.d))

    # Visualizations

    def to_list(self):
        """
        Generate a nested list representing the nodes on each level of the heap.

        @return: A list of lists, where the item in index k is a list of values of the nodes on level k.
        """
        nodes = self[:self.heap_size]
        result = []
        current_level = [0]

        while current_level and nodes:
            next_level = []
            level_nodes = []

            for node_index in current_level:
                level_nodes.append(nodes[node_index])

                children = [child for child in self.get_children_indexes(node_index) if child < self.heap_size]
                next_level.extend(children)

            result.append(level_nodes)
            current_level = next_level
        return result

    def __str__(self):
        return str(self.to_list())

    def print_as_tree(self):
        """
        Print a tree representing the nodes on each level of the heap to the console.
        """
        result = self.to_list()

        if not result:
            print("(Empty heap)\n")
            return

        max_leafs = (self.d ** self.height)
        # The biggest possible bottom level including spaces
        max_width = (max_leafs * (MAX_NODE_VALUE_LENGTH + 2)) + (max_leafs + 1)

        width = max_width // 2
        for level in range(0, len(result)):
            level_nodes = result[level]
            for j in range(len(level_nodes)):
                data = '{node: ^{width}}'.format(node=level_nodes[j], width=width)
                if ((j + 1) % self.d == 0 or (len(level_nodes) <= self.d and level < len(result) - 1)) and j + 1 != len(
                        level_nodes):
                    print(data, end="||")
                else:
                    print(data, end="")

            width = math.ceil(width / self.d)
            print()
        print()  # Buffer space

    def print_as_list(self):
        """
        Print a listing representing the nodes on each level of the heap to the console.
        """
        result = self.to_list()
        for level_num in range(0, len(result)):
            current_level_nodes = result[level_num]
            num_tuples = len(current_level_nodes) // self.d
            node_tuples = [tuple(current_level_nodes[i * self.d: (i + 1) * self.d]) for i in range(num_tuples)]
            if len(current_level_nodes) % self.d != 0:
                node_tuples.append(tuple(current_level_nodes[num_tuples * self.d:]))

            print("- Level {}: {}".format(level_num, node_tuples))
        print()  # Buffer space
