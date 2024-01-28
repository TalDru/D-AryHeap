from dheap import DHeap
from solution import extract_max, extract, insert, increase_key
from common import GeneralAlgorithms

DEFAULT_INPUT_FILE = 'input.txt'


def do_extract_max(heap: DHeap):
    result = extract_max(heap)
    print("\tExtracted max node with value {} from heap.".format(result))


def do_insert(heap: DHeap):
    value = int(input("Input value to insert: "))
    insert(heap, value)


def do_increase_key(heap: DHeap):
    index_to_increase = int(input("Input index to increase: "))
    value = int(input("Input value: "))
    increase_key(heap, index_to_increase, value)


def do_extract(heap: DHeap):
    index_to_remove = int(input("Input index to remove: "))
    removed_node = extract(heap, index_to_remove)
    print("\tExtracted node #{}: {}.".format(index_to_remove, removed_node))


EXIT_KEY = "5"
ACTIONS = {
    "1": ("Extract maximum value", do_extract_max),
    "2": ("Insert value", do_insert),
    "3": ("Increase key", do_increase_key),
    "4": ("Remove key", do_extract),
    EXIT_KEY: ("Exit", None)
}


def get_d_from_user() -> int:
    return int(input("> Insert D for d-heap:"))


def get_file_name_from_user() -> str:
    return input(f"> Input path to file with heap list (default={DEFAULT_INPUT_FILE}): ") or DEFAULT_INPUT_FILE


def get_heap_from_file(file_name: str, d: int) -> DHeap:
    with open(file_name, 'r') as f:
        content = f.read()

    heap_list = [int(num) for num in content.split(",")]
    return DHeap(heap_list, d)


def print_menu():
    print("Possible actions on heap:")
    for key, menu_item in ACTIONS.items():
        print(f"\t{key}. {menu_item[0]}")


def get_menu_option_from_user() -> str:
    # The input loop will run until we get a valid input option
    while True:
        result = input("> Enter action: ")
        if result in ACTIONS:
            return result

        print("Invalid action. Please try again.")


def user_loop():
    d = get_d_from_user()
    filename = get_file_name_from_user()
    heap = get_heap_from_file(filename, d)
    GeneralAlgorithms.build_max_heap(heap)

    while True:
        print_menu()
        menu_option = get_menu_option_from_user()
        if menu_option == EXIT_KEY:
            break

        action = ACTIONS[menu_option][1]
        action(heap)
        heap.print_as_tree()
