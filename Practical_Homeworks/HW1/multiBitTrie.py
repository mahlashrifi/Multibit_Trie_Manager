
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



def print_trie(root, indent=0):
    for child in node.children:
        next_hop_info = ' (Next hop: ' + str(node.children[child].next_hop) + ')' if node.children[child].next_hop is not None else ''
        print('-' * indent + str(child) + next_hop_info)
        print_trie(node.children[child], indent + 4)


    
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



