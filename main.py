"""
D-ary Heap implementation.
@author: Tal Druzhinin & Shelly Goltzman
"""
import math


class DHeap(list):
    def __init__(self, items, d):
        super().__init__()
        for item in items:
            self.append(item)

        self.d = d
        self.heap_size = len(self)

    @property
    def length(self):
        return len(self)

    @property
    def height(self):
        return int(math.floor(math.log(self.heap_size, self.d))) + 1

    def append(self, value):
        list.append(self, value)

    def __setitem__(self, key, value):
        list.__setitem__(self, key, value)

    def swap(self, i, j):
        self[i], self[j] = self[j], self[i]

    def parent(self, k):
        return int(math.floor(k / self.d))

    def nth_child(self, k, n):
        return (self.d * k) + n

    def left(self, k):
        return self.nth_child(k, 1)

    def right(self, k):
        return self.nth_child(k, 2)


def __max_heapify(heap, i):
    # NOT IN THE EXERCISE SCOPE
    children = [heap.nth_child(i, n) for n in range(1, heap.d + 1)]
    largest = i
    for child in children:
        if child < heap.heap_size and heap[child] > heap[largest]:
            largest = child
    if largest != i:
        heap.swap(i, largest)
        __max_heapify(heap, largest)

    # left_node = heap.left(i)
    # right_node = heap.right(i)
    # if left_node < heap.heap_size and heap[left_node] > heap[i]:
    #     largest = left_node
    # else:
    #     largest = i
    # if right_node < heap.length and heap[right_node] > heap[largest]:
    #     largest = right_node
    # if largest != i:
    #     heap.swap(i, largest)
    #     __max_heapify(heap, largest)


def extract_max(heap):
    __max_heapify(heap, 0)
    # Now max is at nodes[0]
    heap.swap(0, heap.heap_size - 1)
    # Now max is at nodes[length]
    heap.heap_size = heap.heap_size - 1
    __max_heapify(heap, 0)  # Fix Heap
    return heap[heap.length]


def insert(self):
    pass


def increase_key(self, i, k):
    # self[i] = k if self[i] < k else self[i]
    pass


def delete(self, i):
    pass


def __heap_to_list(heap: DHeap):
    nodes = list(heap)
    result = []
    current_level = [0]

    while current_level:
        next_level = []
        level_nodes = []

        for node in current_level:
            level_nodes.append(nodes[node])

            children = []
            for n in range(1, heap.d + 1):
                child = heap.nth_child(node, n=n)
                if child < len(nodes):
                    children.append(child)
            next_level.extend(children)

        result.append(level_nodes)
        current_level = next_level
    return result


def __print_heap(heap: DHeap):
    result = __heap_to_list(heap)

    max_leafs = (heap.d ** heap.height)
    max_width = max_leafs * 4 + (max_leafs + 1)

    width = max_width // 2
    for level_nodes in result:
        for j in range(len(level_nodes)):
            node = '{0: ^4}'.format(level_nodes[j])
            data = '{node: ^{width}}'.format(node=node, width=width)
            if ((j + 1) % heap.d == 0 or len(level_nodes) <= heap.d) and j + 1 != len(level_nodes):
                print(data, end="||")
            else:
                print(data, end="")

        width = math.ceil(width / heap.d)
        print()


def main():
    A = DHeap([3, 9, 2, 1, 4, 5, 7, 6, 10, 12, 11], 2)
    print("Height: ", A.height)
    print("Before: ")
    __print_heap(A)
    for i in reversed(range(0, len(A))):
        __max_heapify(A, i)
    print("After: ")
    __print_heap(A)


if __name__ == '__main__':
    main()
