
class Node:
    def __init__(self, next_hob):
        self.left = None
        self.right = None
        self.next_hob = next_hob

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


# len_dict=pre_process(read_input("prefix-list.txt"))
# for key in len_dict:
#     print(f"***************{key}**************")
#     for item in len_dict.get(key):
#         print (f"item = {item}")
# Your existing read_input function remains the same

# def insert(root, prefix, length, next_hob):
#     return "khar"
#
#
# def lookup(root, addr):
#     return "man"
#
# def tprint(root):



