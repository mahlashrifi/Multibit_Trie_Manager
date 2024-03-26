
import time
import tracemalloc
from graphviz import Digraph
from collections import OrderedDict



class Node:
    def __init__(self, next_hop = None, length = 0):
        self.children = {}
        self.next_hop = next_hop
        self.length = length

def read_input(file_name):
    inputs = []
    with open(file_name, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) == 3:
                try:
                    # prefixes are in hex
                    prefix = parts[0]
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

def insert(root, prefix, length, next_hop, stride, base):
    current_node = root  
    integer_prefix = int(prefix[:length],base)
    binary_number = bin(integer_prefix)[2:]

    rjusted = binary_number.rjust(length, '0')
    binary_prefix = rjusted.ljust(32, '0')

    for i in range(0, length, stride):
        bit_pattern = binary_prefix[i:i+stride]
        
        if i + stride > length:
            curr_pattern = str(binary_prefix[i:length]) 
            ex = len(curr_pattern)
            remaining_bits = stride - (length - i)
            # Calculate the number of combinations for the remaining bits
            num_combinations = 2 ** (remaining_bits)
            # Generate all combinations for the remaining bits and create nodes
            for j in range(num_combinations):
                # Generate the binary representation for the current combination
                combination = bin(j)[2:].zfill(remaining_bits)

                pattern = curr_pattern + combination 
                if pattern not in current_node.children:
                    current_node.children[pattern] = Node(next_hop=next_hop, length= length)
                else:
                    if current_node.children[pattern].length < length:
                        current_node.children[pattern].next_hop = next_hop
                        current_node.children[pattern].length = length

        else:

            # If there is no child for the bit pattern, create a new node
            if bit_pattern not in current_node.children:
                current_node.children[bit_pattern] = Node()
            current_node = current_node.children[bit_pattern]
            # If we have reached the end of the prefix, set the next hop

        if (i + stride == length ):
                current_node.next_hop = next_hop
                current_node.length = length
            



def visualize_trie(node, graph=None, parent_name=None, edge_label=''):
    if graph is None:
        graph = Digraph(comment='Trie')

    if parent_name is None:
        parent_name = 'root'
        root_label = str(node.next_hop) if node.next_hop is not None else ''
        graph.node(parent_name, label=root_label)

    sorted_children_keys = sorted(node.children.keys())
  
    # Iterate over the children of the current node
    for bit_pattern in sorted_children_keys:
        child_node = node.children[bit_pattern]
        # The name of the node in the graph is a combination of its parent name and its bit pattern
        node_name = f'{parent_name}-{bit_pattern}'
        
        # If the node has a next_hop value, use it as the label, otherwise leave it blank
        if child_node.next_hop is not None:
            graph.node(node_name, label=str(child_node.next_hop))
        else:
            graph.node(node_name, label='')
        
        # The label for the edge is the bit pattern leading to the current node
        graph.edge(parent_name, node_name, label=bit_pattern)

        # Recursively call visualize_trie to add the children of the current node to the graph
        visualize_trie(child_node, graph, node_name, bit_pattern)

    return graph 

def print_trie(node, file, bit_pattern='', indent=0):
    # Base case: if the current node has a next_hop, write it to the file
    if node.next_hop is not None:
        file.write(' ' * indent + f"Bit pattern: {bit_pattern} -> Next hop: {node.next_hop}\n")

    sorted_children_keys = sorted(node.children.keys())

    # Increase the indentation for child nodes
    new_indent = indent + 4

    # Recursively call print_trie for each child
    for child_bit_pattern in sorted_children_keys:
        child_node = node.children[child_bit_pattern]

        full_bit_pattern = bit_pattern + child_bit_pattern
        file.write(' ' * indent + f"Child bit pattern: {child_bit_pattern}\n")
        print_trie(child_node, file, full_bit_pattern, new_indent)

def lookup(root, ip_address, stride, base):
    binary_ip = bin(int(ip_address, base))[2:].zfill(32)
    current_node = root
    best_match = root.next_hop
    
    for i in range(0, 32, stride):
        bit_pattern = binary_ip[i:i + stride]

        # Check if the bit pattern matches any child of the current node
        if bit_pattern in current_node.children:
            current_node = current_node.children[bit_pattern]

            if current_node.next_hop is not None:
                best_match = current_node.next_hop
        else:
            break  

    return best_match


def run():
    root = Node()
    root.next_hop = None
    stride =8  # Default stride value
    prefix_base = 16 # Default base of prefix

    while True:
     
        command = input("Enter command (Read File, Insert, Print, visualize, Lookup, Set Configuration, Finish): ").strip().lower()

        if command == 'finish':
           
            break

        elif command == 'read file':
            file_name = input("Enter the file name: ")
            start_time = time.time()
            tracemalloc.start() 

            try:
                inputs = read_input(file_name)
                organized_inputs = pre_process(inputs)
                for length in range(0, 33):
                    for prefix, length, next_hop in organized_inputs.get(length, []):
                        if(int(length) == 0):
                            root.next_hop = next_hop
                        else:
                            insert(root, prefix, length, next_hop, stride, prefix_base)
            except FileNotFoundError:
                print(f"File not found: {file_name}")

            end_time = time.time()  # End timing
            print(f"Time taken: {end_time - start_time:.2f} seconds")
            current, peak = tracemalloc.get_traced_memory()
            print(f"Current memory usage: {current / 1024 / 1024:.2f} MB; Peak: {peak / 1024 / 1024:.2f} MB")
            tracemalloc.stop()
   

        elif command == 'insert':
            try:
              
                input_data = input("Enter prefix, length, next_hop: ").split()
                prefix = input_data[0]  
                length, next_hop = map(int, input_data[1:])  

                if(length == 0):
                    root.next_hop = next_hop
                    
                else:    
                    insert(root, prefix, length, next_hop, stride, prefix_base)
            except ValueError:
                print("Invalid input. Please enter three integers separated by spaces.")

        elif command == 'print':
            file_name = input("Enter the file name to print the trie: ")
            with open(file_name, 'w') as file:
                print_trie(root, file)

            print(f"Trie has been printed to {file_name}")

    
        
        elif command == 'lookup':
            try:
                ip_input = input("Enter IP address to lookup: ").strip()
                start_time = time.perf_counter_ns()  # Start timing in nanoseconds

                # Use the IP address input directly in binary format
                next_hop = lookup(root, ip_input, stride, prefix_base)  # Assuming the input is in binary format

                end_time = time.perf_counter_ns()  # End timing in nanoseconds
                lookup_time = end_time - start_time

                print(f"Next hop for {ip_input}: {next_hop}")
                print(f"Lookup time: {lookup_time} nanoseconds")
            except ValueError:
                print("Invalid IP address format. Please enter a valid IP address.")


        elif command == 'set configuration':
            try:
                new_stride = int(input("Enter new stride (1, 2, 4, 8, etc.): "))
                if new_stride > 0:
                    stride = new_stride
                    print(f"Stride set to {stride}")
                else:
                    print("Invalid stride value. Please enter a positive integer.")
                
                # Additional code to set the base for prefix input
                new_base = input("Enter the base for prefix (binary, decimal, hexadecimal): ").strip().lower()
                if new_base in ["binary", "decimal", "hexadecimal"]:
                    if new_base == "binary":
                        prefix_base = 2
                    elif new_base == "decimal":
                        prefix_base = 10
                    elif new_base == "hexadecimal":
                        prefix_base = 16
                    print(f"Base for prefix set to {new_base}")
                else:
                    print("Invalid base. Please enter 'binary', 'decimal', or 'hexadecimal'.")
            except ValueError:
                print("Invalid input. Please enter an integer for stride.")

        elif command == 'visualize':
            g = visualize_trie(root)
            g.render('trie_visualization', view=True, format='png')  # Saves and opens the visualization


run()
