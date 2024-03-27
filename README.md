# Multibit Trie Manager

This project is the culmination of the first practical assignment for the network device course at AUT. With this tool, you can efficiently create, visualize, update, and search within a multibit trie using various configurations.

To become acquainted with multibit trie, please read the following introduction. Additionally, you can access the project definition and implementation report through the corresponding links.

## Introduction

Welcome to the Multibit Trie Manager!

In the realm of networking, the Multibit Trie stands as a formidable structure, offering an elegant solution to the complexities of IP address lookup. Imagine a world where the vast expanse of IP addresses is organized into a streamlined hierarchy, readily accessible for efficient routing and navigation. This is where the Multibit Trie shines, meticulously breaking down IP addresses into smaller, more manageable bits, and arranging them within a trie structure.

**Why Multibit Trie?**

The beauty of the Multibit Trie lies in its ability to accelerate search operations with unparalleled efficiency. By harnessing the power of trie organization, IP lookup operations are transformed into lightning-fast endeavors, ensuring optimal performance in routing tables and networking devices. With its hierarchical architecture, Multibit Trie guarantees logarithmic time complexity, minimizing search times and optimizing network performance.

**Understanding Multibit Trie**

At its core, the Multibit Trie represents a leap forward from its binary counterpart. Unlike binary tries, where each node has a binary choice, Multibit Trie embraces diversity, allowing nodes to have multiple children based on a predefined stride. For instance, with a stride of 3, each node can accommodate up to 8 children, leading to a more compact trie structure. However, this compactness comes with a trade-off—each child node boasts a more intricate data structure to manage its offspring.

**Trie vs. Tree**

In the vast landscape of data structures, the Multibit Trie stands as a specialized tool tailored for specific tasks like IP address lookup. While general-purpose trees offer versatility, Multibit Trie excels in the efficient retrieval of sequences, making it a go-to choice for tasks requiring rapid and precise navigation through key-based data.

With this understanding, let's delve deeper into the functionalities and usage of the Multibit Trie Manager!


## How to Use

1. **Clone the program**.
2. **Install Graphviz for visualization**: `pip install Graphviz` ([Graphviz](https://graphviz.org/))%.
3. **Run the application**.
4. Upon running the application, you will encounter the following menu*:

   To use the application effectively, familiarize yourself with the following commands (commands are not case-sensitive):
   
   1. **Set Configuration**: Here, you can set the base and stride of the trie. Input options include binary, decimal, and hexadecimal.
   
   2. **Read File**: Input nodes can be obtained from a file. For example, refer to this [example file](example.txt)%.
   
   3. **Insert**: Add a new IP address to the trie.
      - *Prefix*: Prefix of the IP address (host).
      - *Length*: Number of meaningful digits in the set base. For instance, if prefix = 4 and length = 2 with a base of binary, it means our host number = [insert example here].
   
   4. **Visualize**: Display the result of your trie. After using this command, you can add nodes to your trie again.
   
   5. **Print**: Show the trie by printing its information.
   
   6. **Lookup**: Find a prefix in the trie (IP address lookup). It will return the next hop for the entered prefix and the execution time*.
   
   7. **Finish**: Terminate execution.

   *Suggestion*: When using the insert command, it is advisable to first write the entries in a file and then enter them all at once. This practice makes it easier to identify any issues with the trie. For example, refer to [example.txt](example.txt)% designed for drawing the trie described in the project definition.

## Screenshots

Results of trie creation and visualization for the project definition example with different strides:

- ![Stride = 1](path/to/image1.png)*
- ![Stride = 2](path/to/image2.png)*
- ![Stride = 4](path/to/image3.png)*
- ![Stride = 8](path/to/image4.png)*

The printed result of this example exists in the Result folder.
