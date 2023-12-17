
import time
import tracemalloc
from graphviz import Digraph

class Node:
    def __init__(self, next_hop = None):
        self.children = {}
        self.next_hop = next_hop

def read_input(file_name):
    inputs = []
    with open(file_name, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) == 3:
                try:
                    # prefixes are in hex
                    prefix = int(parts[0], 16)
                    length = int(parts[1])
                    next_hop = int(parts[2])
                    inputs.append((prefix, length, next_hop))
                except ValueError:
                    # Handle the case where conversion to int fails
                    print(f"Invalid line format(not able to change to string): {line.strip()}")
    return inputs


##This function will sort inputs for more efficent creation of trie
def pre_process(inputs):
    # ipv4 is 32 bit. hence length is between 0 to 32
    length_dict = {length: [] for length in range(0, 33)}

    for prefix, length, next_hop in inputs:
        length_dict[length].append([prefix, length, next_hop])
    
    for length in length_dict:
        length_dict[length].sort(key=lambda x: x[0])
    
    return length_dict

# Convert integer to a 32-bit binary string
def int_to_binary_str(prefix, max_length=32):

    return bin(prefix)[2:].zfill(max_length)

def insert(root, stride, prefix, length, next_hop):
    current_node = root  
    binary_prefix = int_to_binary_str(prefix)  

    for i in range(0, length, stride):
        # Extract the part of the prefix corresponding to the current stride
        bit_pattern = binary_prefix[i:i+stride]
        
        # If there is no child for the bit pattern, create a new node
        if bit_pattern not in current_node.children:
            current_node.children[bit_pattern] = Node()
        
        current_node = current_node.children[bit_pattern]
    
        # If we have reached the end of the prefix, set the next hop
        if i + stride >= length:
            current_node.next_hop = next_hop
            break





# Call the print_trie function after the trie has been constructed
# ... (rest of your code)


# Call the print_trie function after the trie has been constructed

# inputs = read_input("prefix-list.txt")
# organized_inputs = pre_process(inputs)
# root = Node()
# for length in range(0, 33):
#     for prefix, length, next_hop in organized_inputs.get(length):
#         insert(root, 2, prefix, length, next_hop)
# print_trie(root)
    
def lookup(root, addr, stride):
    current_node = root
    binary_addr = int_to_binary_str(int(addr, 16))  # Assuming addr is a hex string

    last_next_hop = None
    i = 0
    while i < len(binary_addr):
        if current_node.next_hop is not None:
            last_next_hop = current_node.next_hop

        bit_pattern = binary_addr[i:i+stride]

        if bit_pattern in current_node.children:
            current_node = current_node.children[bit_pattern]
            i += stride
        else:
            break

    return last_next_hop


def visualize_trie(node, graph=None, parent_name=None, edge_label=''):
    if graph is None:
        graph = Digraph(comment='Trie')

    if parent_name is None:
        parent_name = 'root'

    for bit_pattern, child_node in node.children.items():
        node_name = f'{parent_name}-{bit_pattern}'
        graph.node(node_name, label=bit_pattern + (f'\n({child_node.next_hop})' if child_node.next_hop is not None else ''))
        graph.edge(parent_name, node_name, label=edge_label)

        visualize_trie(child_node, graph, node_name, bit_pattern)

    return graph

def print_trie(node, indent=0):
    for child in node.children:
        next_hop_info = ' (Next hop: ' + str(node.children[child].next_hop) + ')' if node.children[child].next_hop is not None else ''
        print('-' * indent + str(child) + next_hop_info)
        print_trie(node.children[child], indent + 4)

def run():
    root = Node()
    stride = 2  # Default stride value

    while True:
        start_time = time.time()
        tracemalloc.start() 

        command = input("Enter command (Read File, Insert, Print, Lookup, Set Stride, Finish): ").strip().lower()

        if command == 'finish':
            end_time = time.time()  # End timing
            print(f"Time taken: {end_time - start_time:.2f} seconds")
            current, peak = tracemalloc.get_traced_memory()
            print(f"Current memory usage: {current / 1024 / 1024:.2f} MB; Peak: {peak / 1024 / 1024:.2f} MB")
            tracemalloc.stop()
            break

        elif command == 'read file':
            file_name = input("Enter the file name: ")
            try:
                inputs = read_input(file_name)
                organized_inputs = pre_process(inputs)
                for length in range(0, 33):
                    for prefix, length, next_hop in organized_inputs.get(length, []):
                        insert(root, prefix, length, next_hop, stride)
            except FileNotFoundError:
                print(f"File not found: {file_name}")

        elif command == 'insert':
            try:
                prefix, length, next_hop = map(int, input("Enter prefix, length, next_hop: ").split())
                insert(root, prefix, length, next_hop, stride)
            except ValueError:
                print("Invalid input. Please enter three integers separated by spaces.")

        elif command == 'print':
            print_trie(root)

        elif command == 'lookup':
            try:
                addr = int(input("Enter address to lookup (in hex): "), 16)
                next_hop = lookup(root, addr, stride)
                print(f"Next hop for {addr:0X}: {next_hop}")
            except ValueError:
                print("Invalid address format. Please enter a hexadecimal address.")

        elif command == 'set configuration':
            try:
                new_stride = int(input("Enter new stride (2, 4, 8, etc.): "))
                if new_stride > 0:
                    stride = new_stride
                    print(f"Stride set to {stride}")
                else:
                    print("Invalid stride value. Please enter a positive integer.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

        elif command == 'visualize':
            g = visualize_trie(root)
            g.render('trie_visualization', view=True, format='png')  # Saves and opens the visualization



        

run()
