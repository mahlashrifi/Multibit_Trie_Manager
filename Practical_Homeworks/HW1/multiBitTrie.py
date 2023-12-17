
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

inputs = read_input("prefix-list.txt")
organized_inputs = pre_process(inputs)
root = Node()
for length in range(0, 33):
    for prefix, length, next_hop in organized_inputs.get(length):
        insert(root, 2, prefix, length, next_hop)


def tprint(root):
#
#
# def lookup(root, addr):
#     return "man"
#
# def tprint(root):



