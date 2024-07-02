# EDCN-Determination Program
This repository provides code for finding the edge-distinguishing chromatic number of a graph. Using an adjacency list as a repsresentation of a graph, this program will accurately determine the EDCN of the graph.

We will now discuss the necessary program inputs as well as an analysis of the output. Please feel free to ask questions about the methods.

## Transform a Graph into an Adjacency List
In order for the code to be able to calculate the EDCN, the graph must first be entered into the code. Line 61 of the code asks for the graph, and this is where the adjacency list will go. In order to represent your graph as an adjacency list, please do the following. Assume that you have a graph of $n$ vertices.

1. Start with an empty list.
2. Label each vertex in your graph a unique number 0, 1, 2, ..., $(n-1)$.
3. Starting at vertex 0, create list of all vertices that are adjacent to vertex 0. For example, if vertex 0 was adjacent to vertex 1 and 2, the list for vertex 0 would be $[1, 2]$.
4. Add this list to the blank list you created at the start.
5. Repeat steps 3 and 4 for all vertices.
6. Your final list should have as many terms as there are vertices in your graph.

This adjacency list allows the program to recognize what vertices are neighbors with each other, and therefore it can easily determine what the induced edge colors are. Once the adjacency list is entered, feel free to run the code.

## Program Output
After the program has run, it will output two answers, both of which are labeled, but we will still describe them here. The first output tells you what the EDCN of the graph is. This is pretty straightforward. The second output is the vertex colors. This line of numbers is the color of the vertices for a proper $k$-coloring of your graph. The numbers are in the same order as your adjacency list. This means that the first number is the color of vertex 0, the second number is the color of vertex 1, and so on. There are many other proper $k$-colorings of the graph, but this is the one that the program calculated the EDCN on.

## Versions
python: 3.10.6
