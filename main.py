"""
D-ary Heap implementation.
@author: Tal Druzhinin & Shelly Goltzman
"""
import math


class DHeap(list):
    def __init__(self, items, d):
        super().__init__()
        self.heap_size = 0
        for item in items:
            self.heap_size += 1
            self.append(item)

        self.length = self.heap_size

        self.d = d

    def __len__(self):
        return self.heap_size

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

    def nth_child_index(self, k, n):
        return (self.d * k) + n

    def left(self, k):
        return self.nth_child_index(k, 1)

    def right(self, k):
        return self.nth_child_index(k, self.d)


def __max_heapify(heap: DHeap, root_index):
    # NOT IN THE EXERCISE SCOPE
    children_indexes = [heap.nth_child_index(root_index, n) for n in range(1, heap.d + 1)]
    largest_index = root_index
    for child_index in children_indexes:
        if child_index < heap.heap_size and heap[child_index] > heap[largest_index]:
            largest_index = child_index
    if largest_index != root_index:
        heap.swap(root_index, largest_index)
        __max_heapify(heap, largest_index)

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


def extract_max(heap: DHeap):
    """
    Extract max node assuming `heap` is a max heap (and therefore max var is at index 0).

    @param heap: DHeap object
    @type heap: C{DHeap}
    @return: Max node value
    """
    heap.swap(0, heap.heap_size - 1)
    # Now max is at heap[heap.heap_size - 1]
    popped_node = heap[heap.heap_size - 1]
    heap.heap_size = heap.heap_size - 1
    __max_heapify(heap, 0)  # Fix Heap
    return popped_node


def insert(self):
    pass  # TODO Tal


def increase_key(self, i, k):
    # self[i] = k if self[i] < k else self[i]
    pass  # TODO Shelly


def pop(heap: DHeap, index_to_delete):
    heap.swap(index_to_delete, heap.heap_size - 1)
    # Now max is at heap[heap.heap_size - 1]
    popped_node = heap[heap.heap_size - 1]
    heap.heap_size = heap.heap_size - 1
    for i in reversed(range(0, heap.heap_size)):
        __max_heapify(heap, i)  # Fix Heap
    return popped_node


def __heap_to_list(heap: DHeap):
    nodes = list(heap)[:heap.heap_size]
    result = []
    current_level = [0]

    while current_level:
        next_level = []
        level_nodes = []

        for node in current_level:
            level_nodes.append(nodes[node])

            children = []
            for n in range(1, heap.d + 1):
                child = heap.nth_child_index(node, n=n)
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
    A = DHeap([3, 9, 2, 1, 4, 5, 7, 6, 10, 12, 11], 3)
    print("Height: ", A.height)

    print("Before: ")
    print(list(A))
    __print_heap(A)

    for i in reversed(range(0, len(A))):
        __max_heapify(A, i)

    print("After: ")
    print(list(A))
    __print_heap(A)

    print("After extract_max: ")
    max_node = extract_max(A)
    print(list(A), "Max node:", max_node)
    __print_heap(A)

    print("After pop: ")
    popped_index = 2
    popped_node = pop(A, popped_index)
    print(list(A), "Popped node on {}: {}".format(popped_index, popped_node))
    __print_heap(A)


if __name__ == '__main__':
    main()

# TODO S - get D from user
# TODO S - get heap input from file
# TODO T - Add docstrings to all functions
# TODO implement all public functions
# TODO S+T - write down a pseudocode algorythm for each function (including private)
# TODO S+T - analyze runtime complexity of each public function
# TODO S - make printing work better with larger trees
# TODO S - optional - make printing prettier
# TODO T - move all misc functions to an auxiliary file
