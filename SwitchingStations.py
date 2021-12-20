# Ryan Knapp
# CS590 Algorithms Reza Peyrovian
# Minimum Spanning Tree Application Assignment
# December 15, 2021

import sys

# Set TestingTheProgram to True to run the test case or False to run main.
TestingTheProgram = False

def input_adjacency_list(vertex):

    graphResult = []

    for i in range(vertex):

        adj = [int(x) for x in
             input("Enter list for vertex " + str(i) + " (in list format separated by spaces): ").split(' ')]
        graphResult.append(adj)

    for adjList in graphResult:
        print(adjList)

    confirmation = input("\nPlease type 'go' if you would like to input the above matrix: ")

    if confirmation.lower() == 'go':
        return graphResult
    else:
        return input_adjacency_list(vertex)

# function for building the MST
def BuildMaximumSpanningTree(N, G):

    chosenVertex = []

    for i in range(N):
        chosenVertex.append(0)

    edge = 0
    chosenVertex[0] = True

    MSTGraph = []

    # print statement outputting the edges and weights for the tree
    while edge < N - 1:
        max = 0
        source = 0
        dest = 0
        for d in range(N):
            if chosenVertex[d]:
                for n in range(N):
                    if (not chosenVertex[n]) and G[d][n]:
                        if max < G[d][n]:
                            max = G[d][n]
                            source = d
                            dest = n

        print("Edge = [" + str(source) + ", " + str(dest) + "]  |  Weight = " + str(G[source][dest]))

        MSTGraph.append([source, dest, G[source][dest]])
        chosenVertex[dest] = True
        edge = edge + 1

    output = []
    for n in range(N):
        dummy = []
        for i in range(N):
            dummy.append(0)
        output.append(dummy)

    for edges in MSTGraph:
        output[edges[0]][edges[1]] = edges[2]
        output[edges[1]][edges[0]] = edges[2]

    print("*****************************************************************")
    print("The output graph is as follows: \n")

    for adjList in output:
        print(adjList)
    return output

# DFS search function searching for path between stations a and b
def pathSearch(Graph, source, dest, weight, vertices=[]):
    if not bool(vertices):
        adjList = []
        for j in range(len(Graph[source])):
            adjList.append(0)
        for i in range(len(Graph[source])):
            vertices.append(adjList)

    if (Graph[source][dest] != 0) and (vertices[source][dest] != 1):
        if Graph[source][dest] < weight:
            weight = Graph[source][dest]
        vertices[source][dest] = 1
        return weight

    else:
        for i in range(len(Graph[source])):
            if (Graph[source][i] != 0) and vertices[source][i] != 1:
                vertices[source][i] = 1
                if Graph[source][i] < weight:
                    weight = Graph[source][i]
                n = pathSearch(Graph, i, dest, weight, vertices)
                if n < weight:
                    weight = n
        return weight

def main():

    # error handling to make sure that the input is an integer
    error = True

    vertex = 0
    while error:
        dummy = input('Enter the number of vertices for your graph:')
        if dummy.isdigit():
            error = False
            vertex = int(dummy)
        else:
            print("This input does not work! Enter an integer please!\n")

    print("\nThe following graph contains " + str(vertex) + " vertices.")

    Graph = input_adjacency_list(vertex)
    MaxSpanGraph = BuildMaximumSpanningTree(vertex, Graph)

    SwitchA = int(input("Enter value for the source switching center node A (enter integer): "))
    SwitchB = int(input("Enter value for the destination switching center node B (enter integer): "))

    bandwidthMax = pathSearch(MaxSpanGraph, SwitchA, SwitchB, sys.maxsize)
    print("********************************************************************************")
    print("\nThe maximum bandwidth between switches with node values " + str(SwitchA) + " and " + str(SwitchB) + " = " + str(bandwidthMax))

def test_program():

    testInputGraph = [[8, 15, 6, 8], [15, 8, 6, 9], [6, 6, 8, 1], [8, 9, 1, 8]]

    print("The results of our test program are as follows: ")
    MaxSpanGraph = BuildMaximumSpanningTree(4, testInputGraph)

    # take in user input for both switching centers
    SwitchA = int(input("Enter value for the source switching center node A (enter integer): "))
    SwitchB = int(input("Enter value for the source switching center node B (enter integer): "))

    # calculates the maximum bandwidth between switching station A and switching station B given the user input
    bandwidthMax = pathSearch(MaxSpanGraph, SwitchA, SwitchB, sys.maxsize)
    print("********************************************************************************")
    print("\nThe maximum bandwidth between switches with node values " + str(SwitchA) + " and " + str(SwitchB) + " = " + str(bandwidthMax))

# if we are not testing the program, then we run main. If we are testing, we run our test_program method
if not TestingTheProgram:
    main()
else:
    test_program()
