# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 10:46:15 2019

@author: spencer.stewart
"""

from collections import defaultdict

# hold a map from vertex (int) to a boolean indicated if we have
# visited that node.
visited = {}

def previsit(v):
    print("Visiting: %s" % v)

def postvisit(v):
    print("done Visiting: %s" % v)

def explore(gGraph, vNode, visited, invertedGraph):
    """
    
    Explore the unexplored vertices of gGraph starting at vNode
    
    gGraph: adjacency matrix for undirected graph
    vNode: a node to start exploring from (an index)
    
    a -> b, c, d
    
    b -> a You want to to append a to the end of b
    c -> a You want to to append a to the end of c
    d -> a You want to to append a to the end of d
    
    """
    
    visited[vNode] = True
    tempList = []
    
    previsit(vNode)

    for nextNode in gGraph[vNode]:
        print("This is nextNode:", nextNode)
        if not visited[nextNode]:
            invertedGraph = explore(gGraph, nextNode, visited, invertedGraph)

        invertedGraph[nextNode].extend([vNode])





    print("This is postvisit 0:", invertedGraph[0])
    print("This is postvisit 1:", invertedGraph[1])
    print("This is postvisit 2:", invertedGraph[2])
    print("This is postvisit 3:", invertedGraph[3])
    print("This is postvisit 4:", invertedGraph[4])
    print("This is postvisit 5:", invertedGraph[5])
    print("This is postvisit 6:", invertedGraph[6])
    print("This is postvisit 7:", invertedGraph[7])



    postvisit(vNode)

    return invertedGraph
    
def depthFirstSearch(gGraph):

    # Create the globol variable of whether a function is limit or not.
    globals()['visited'] = {}

    # Determine the length of the visited catalog.
    visited = [False] * len(gGraph)

    invertedGraph = defaultdict(list)

    # Start at first node and visit all other nodes
    for nextNode in range(len(gGraph)):
        if not visited[nextNode]:
            invertedGraph = explore(gGraph, nextNode, visited, invertedGraph)

    print("This is inverted graph:", invertedGraph[0])

    #
    # invertedGraph[1].sort()
    # invertedGraph[2].sort()

    return invertedGraph

            
#def adjacencyListCreation(passedList):


    
    
##############################################################
#                            Tests                           #
##############################################################
    
    

    
def test_adjacencyListCreation_Tests():
    
    testGraph1 = defaultdict(list)
    testGraph2 = defaultdict(list)
    testGraph3 = defaultdict(list)
    testGraph4 = defaultdict(list)

    testGraph1Expected = defaultdict(list)
    testGraph2Expected = defaultdict(list)
    testGraph3Expected = defaultdict(list)
    testGraph4Expected = defaultdict(list)

    testGraph1[0].extend([1,4])
    testGraph1[1].extend([3])
    testGraph1[2].extend([5])
    testGraph1[3].extend([])
    testGraph1[4].extend([6,7])
    testGraph1[5].extend([])
    testGraph1[6].extend([0])
    testGraph1[7].extend([2])
    
    # testGraph2[0].extend([2,5,6])
    # testGraph2[1].extend([1,5,6])
    # testGraph2[2].extend([6,7])
    # testGraph2[3].extend([2,4,5])
    # testGraph2[4].extend([1,3])
    #
    # testGraph3[0].extend([5,6,7])
    # testGraph3[1].extend([1,3,5])
    # testGraph3[2].extend([4,6])
    # testGraph3[3].extend([5,6])
    # testGraph3[4].extend([1,6,7])

    testGraph4[0].extend([1])
    testGraph4[1].extend([2, 3, 4])
    testGraph4[2].extend([5])
    testGraph4[3].extend([])
    testGraph4[4].extend([1])
    testGraph4[5].extend([2])

    testGraph1Expected = depthFirstSearch(testGraph1)
    # testGraph2Expected = depthFirstSearch(testGraph2)
    # testGraph3Expected = depthFirstSearch(testGraph3)
    testGraph4Expected = depthFirstSearch(testGraph4)



    assert testGraph1Expected[0] == [6]
    assert testGraph1Expected[1] == [0]
    assert testGraph1Expected[2] == [7]
    assert testGraph1Expected[3] == [1]
    assert testGraph1Expected[4] == [0]
    assert testGraph1Expected[5] == [2]
    assert testGraph1Expected[6] == [4]
    assert testGraph1Expected[7] == [4]


    assert testGraph4Expected[0] == []
    assert testGraph4Expected[1] == [0, 4]
    assert testGraph4Expected[2] == [1, 5]
    assert testGraph4Expected[3] == [1]
    assert testGraph4Expected[4] == [1]
    assert testGraph4Expected[5] == [2]




def test_multipleExtension():

    gGraph = defaultdict(list)

    gGraph[5].extend([1])
    gGraph[5].extend([2])

    assert gGraph[5] == [1, 2]


def test_listAdding():

    list1 = [1]
    list2 = [2]

    list2 = list2 + list1

    list2.sort()

    assert list2 == [1, 2]



    #if __name__ == "__main__":
def main():

    gGraph = defaultdict(list)

    gGraph[0].extend([1,2])
    gGraph[1].extend([0,3,4])
    gGraph[2].extend([0,3])
    gGraph[3].extend([1,2,4])
    gGraph[4].extend([1,3])

    depthFirstSearch(gGraph)



    assert depthFirstSearch(gGraph) == (0,1,3,2,2,4,4,3,1,0)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    