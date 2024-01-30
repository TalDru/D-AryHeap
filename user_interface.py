"""
This files contains the UI wrapper for the main assignment,
allowing access to the functions from a console interface.

@author: Tal Druzhinin & Shelly Goltzman
"""
from common import GeneralAlgorithms
from dheap import DHeap
from solution import extract_max, extract, insert, increase_key

DEFAULT_INPUT_FILE = 'input.txt'
MAX_TREE_DISPLAY_ITEMS = 32


def safe_input_int(prompt: str):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Input has to be a number. Please try again.")


def do_extract_max(heap: DHeap):
    result = extract_max(heap)
    print("\tExtracted max node with value {} from heap.".format(result))


def do_insert(heap: DHeap):
    value = safe_input_int("\t>Input value to insert: ")
    insert(heap, value)


def do_increase_key(heap: DHeap):
    index_to_increase = safe_input_int("\t>Input index to increase: ")
    value = safe_input_int("\t>Input value: ")
    increase_key(heap, index_to_increase, value)


def do_extract(heap: DHeap):
    index_to_remove = safe_input_int("\t>Input index to remove: ")
    removed_node = extract(heap, index_to_remove)
    print("\tExtracted node #{}: {}.".format(index_to_remove, removed_node))


RELOAD_HEAP_KEY = "5"
EXIT_KEY = "6"
ACTIONS = {
    "1": ("Extract maximum value", do_extract_max),
    "2": ("Insert value", do_insert),
    "3": ("Increase key", do_increase_key),
    "4": ("Remove key", do_extract),
    RELOAD_HEAP_KEY: ("Load different heap", None),
    EXIT_KEY: ("Exit", None)
}


def get_d_from_user() -> int:
    return int(input("> Insert D for d-heap:"))


def get_file_name_from_user() -> str:
    return input(f"> Input path to file with heap list (default={DEFAULT_INPUT_FILE}): ") or DEFAULT_INPUT_FILE


def get_list_from_file(file_name: str) -> list:
    with open(file_name, 'r') as f:
        content = f.read()

    input_list = [int(num) for num in content.split(",")]
    return input_list


def load_heap():
    d = get_d_from_user()
    filename = get_file_name_from_user()
    print(f"Reading heap from path {filename}...")
    input_list = get_list_from_file(filename)
    print(f"Got list (size {len(input_list)}): {input_list}")
    heap = DHeap(input_list, d)
    print("Converting into Max Heap...")
    GeneralAlgorithms.build_max_heap(heap)
    print("Heap is ready!\n--------------\n")
    return heap


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
    heap = load_heap()

    while True:
        if heap.heap_size > MAX_TREE_DISPLAY_ITEMS:
            print("Heap is too big to print as a tree, Heap will be displayed as list.")
            heap.print_as_list()
        else:
            heap.print_as_tree()

        print_menu()
        menu_option = get_menu_option_from_user()
        if menu_option == EXIT_KEY:
            print("Exiting...")
            break
        elif menu_option == RELOAD_HEAP_KEY:
            heap = load_heap()
        else:
            action = ACTIONS[menu_option][1]
            action(heap)
