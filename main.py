"""
D-ary Heap implementation.
@author: Tal Druzhinin & Shelly Goltzman
"""


class DAryHeap:
    def __init__(self, nodes, heap_size):
        self.nodes = nodes or []
        self.heap_size = heap_size
        self.length = len(self.nodes)

    def __swap(self, i, j):
        self.nodes[i], self.nodes[j] = self.nodes[j], self.nodes[i]

    def __max_heapify(self):
        # NOT IN THE EXERCISE SCOPE
        self.nodes.sort()

    def extract_max(self):
        self.__max_heapify()
        # Now max is at nodes[0]
        self.__swap(0, self.heap_size - 1)
        # Now max is at nodes[length]
        self.heap_size = self.heap_size - 1
        self.__max_heapify()  # Fix Heap
        return self.nodes[len(self.nodes)]

    def insert(self):
        pass

    def increase_key(self, i, k):
        # self[i] = k if self[i] < k else self[i]
        pass

    def delete(self, i):
        pass


def main():
    pass


if __name__ == '__main__':
    main()
