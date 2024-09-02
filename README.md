

# Multibit Trie Manager

This project is the first project for the Network Device Course at AUT, undertaken in Fall 2023. With this tool, you can efficiently create, visualize, update, and search within a multibit trie using various configurations.


## Introduction

The Multibit Trie revolutionizes IP address lookup with its efficient organization and lightning-fast search capabilities. By breaking down IP addresses into manageable bits within a trie structure, it optimizes routing tables and networking devices, ensuring rapid and precise navigation through hierarchical architecture. Its versatility extends beyond networking to various applications requiring efficient key-based data retrieval.

**Multibit trie structure**


The Multibit Trie is an advanced version of the binary trie, enabling each node to have more than two children based on the address bit division, known as the stride. For example, with a stride of 2, each node can accommodate up to 4 children. This structure results in a more compact trie. However, this advantage requires a more complex data structure for each child node. Examples of Multibit Trie with different strides can be found [here](#screenshots)


**Trie vs. Tree**

A general-purpose tree can store any data type—numbers, strings, objects, whereas a trie is specifically used for storing sequences, like strings or arrays.

## How to Use the tool

For visualization, the Graphviz tool has been utilized. Before running the application, you need to download this tool from [here](https://graphviz.org/download/), then use `pip install Graphviz` for installation.

Upon running the application, you will encounter the following menu:

![menu](https://github.com/mahlashrifi/Multibit_Trie_Manager/blob/master/screen-shots/main-menu.png)

1. **Set Configuration**: Here, you can set the base and stride of the trie. Base input options include binary, decimal, and hexadecimal.

2. **Read File**: Input nodes can be obtained from a file. For example, you can find a file which is based on hexadecimal [here](https://github.com/mahlashrifi/Multibit_Trie_Manager/blob/master/prefix-list.txt).

3. **Insert**: Add a new IP address to the trie.
    ![Insert menu example](https://github.com/mahlashrifi/Multibit_Trie_Manager/blob/master/screen-shots/insert-command.png)
    - *Prefix*: Prefix of the IP address (host).
    - *Length*: Number of meaningful digits in the set base.
    - *Next Hop*: Next hop of corresponding prefix.

4. **Visualize**: Display the result of your trie. After using this command, you can add nodes to your trie again.

5. **Print**: Show the trie by printing its information.

6. **Lookup**: Find a prefix in the trie (IP address lookup). It will return the next hop for the entered prefix and the time it took to find the next hop.
    ![Lookup result example](https://github.com/mahlashrifi/Multibit_Trie_Manager/blob/master/screen-shots/lookup_result.png)

7. **Finish**: Terminate execution.

*Suggestion*: When using the insert command, it is advisable to first write the entries in a file and then enter them all at once. This practice makes it easier to identify any issues with the trie. For example, refer to [example.txt](https://github.com/mahlashrifi/Multibit_Trie_Manager/blob/master/example.txt) designed for drawing the trie described in the project definition.

![Trie](https://github.com/mahlashrifi/Multibit_Trie_Manager/blob/master/screen-shots/project-definition-trie.png)




## Screenshots

Results of trie creation and visualization for the project definition example with different strides:

- ![Stride = 1](https://github.com/mahlashrifi/Multibit_Trie_Manager/blob/master/screen-shots/res-stride1.png)
- ![Stride = 2](https://github.com/mahlashrifi/Multibit_Trie_Manager/blob/master/screen-shots/res-stride2.png)
- ![Stride = 4](https://github.com/mahlashrifi/Multibit_Trie_Manager/blob/master/screen-shots/res-stride4.png)
- ![Stride = 8](https://github.com/mahlashrifi/Multibit_Trie_Manager/blob/master/screen-shots/res-stride8.png)

The printed result of this example exists in the Result folder.
