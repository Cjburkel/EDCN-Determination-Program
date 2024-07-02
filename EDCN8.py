
from typing import List, Set
from itertools import product


def graph_coloring(graph, m):
    blank_graph = []
    for i in range(len(graph)):   #need to add all the possible colors to the empty graph
        blank_graph.append(i)
    best_edcn = len(graph) + 1
    best_coloring = ()
    for p in product(blank_graph, repeat = len(blank_graph)):    #creates all permutations with repetition of colored boards
        if is_safe(graph, p):
            if max(p) < best_edcn:          #no need to have a legal list, just pull the info straight from each individual board
                best_edcn = max(p)          #should cut down on run time since there is no need to store the memory of each board
                best_coloring = p
    return [list(best_coloring), best_edcn]
        
def is_safe(graph, board):
    colors = list(board)
    v = 0
    neighbor_colors = []
    neighbor_colors_check = []
    reverse_neighbor_colors = []
    reverse_neighbor_colors_check = []
    duplicate_counter = 0
    while v < len(graph):          #need to get a variable to rotate through all indices of the graph
        for neighbor in graph[v]:    #add the edge colors to their respective lists
            distinguished_color = [colors[v], colors[neighbor]]
            reverse_distinguished_color = [colors[neighbor], colors[v]]
            if duplicate_check(distinguished_color):
                neighbor_colors.append(distinguished_color)
                reverse_neighbor_colors.append(reverse_distinguished_color)
                duplicate_counter += 0.5        #this is necessary because edge colors such as {1, 1} get counted twice
            else:
                neighbor_colors.append(distinguished_color)
                reverse_neighbor_colors.append(reverse_distinguished_color)
        v += 1
    for r in neighbor_colors:              #this is really where the legal checking is going on
        if r not in neighbor_colors_check:
            neighbor_colors_check.append(r)
    for q in reverse_neighbor_colors:
        if q not in reverse_neighbor_colors_check:
            reverse_neighbor_colors_check.append(q)  #this line of code below is seeing if there are any duplicated edges, accounting for the colors like {1, 1}
    if len(neighbor_colors) - len(neighbor_colors_check) == duplicate_counter and len(reverse_neighbor_colors) - len(reverse_neighbor_colors_check) == duplicate_counter:
        return True
    else:
        return False
    
def duplicate_check(dcolor):   #sees if an edge coloring is like {c, c}
    colorsv = dcolor[0]
    colorsn = dcolor[1]
    if colorsv == colorsn:
        return True
    else:
        return False
    
    
if __name__ == "__main__":
    # Sample graph represented as an adjacency list
    graph = [[1, 4, 5, 6],[0, 2, 6],[1, 3, 6],[2, 4, 5],[0, 3, 5],[0, 3, 4], [0, 1, 2]]

    # Set the maximum number of colors
    max_colors = len(graph)

    # Find and output the edcn. Everything is +1 because the list will be returned in 0-based numbering. Just need to shift up 1
    edcn = graph_coloring(graph, max_colors)
    print("Edge Distinguishing Chromatic Number:", edcn[1] + 1)
    
    print("Vertex colors:", end=" ")
    for j in edcn[0]:
        print(j + 1, end = " ")