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
    #print("Visiting: %s" % v)
    print(v)

def postvisit(v):
    #print("done Visiting: %s" % v)
    print(v)

def explore(gGraph, vNode, visited):
    """
    
    Explore the unexplored vertices of gGraph starting at vNode
    
    gGraph: adjacency matrix for undirected graph
    vNode: a node to start exploring from (an index)
    
    """
    
    visited[vNode] = True
    
    previsit(vNode)
    
    for b in gGraph[vNode]:
        if not visited[b]:
            explore(gGraph, b, visited)
            
    postvisit(vNode)
    
def depthFirstSearch(gGraph):
    
    globals()['visited'] = {}
    
    visited = [False] * len(gGraph)
    
    for v in range(len(gGraph)):
        if not visited[v]:
            explore(gGraph, v, visited)
            
#def adjacencyListCreation(passedList):


    
    
##############################################################
#                            Tests                           #
##############################################################
    
    
    #if __name__ == "__main__":
def test_main():
    
    gGraph = defaultdict(list)
    
    gGraph[0].extend([1,2])
    gGraph[1].extend([0,3,4])
    gGraph[2].extend([0,3])
    gGraph[3].extend([1,2,4])
    gGraph[4].extend([1,3])
    
    depthFirstSearch(gGraph)
    
    assert depthFirstSearch(gGraph) == (0,1,3,2,2,4,4,3,1,0)
    
    
def test_adjacencyListCreation_Tests():
    
    testGraph1 = defaultdict(list)
    testGraph2 = defaultdict(list)
    testGraph3 = defaultdict(list)
    
    testGraph1[0].extend([1,4,5])
    testGraph1[1].extend([1,2,3])
    testGraph1[2].extend([4,6])
    testGraph1[3].extend([1,2,4,6,7])
    testGraph1[4].extend([2,5,6,7])
    
    testGraph2[0].extend([2,5,6])
    testGraph2[1].extend([1,5,6])
    testGraph2[2].extend([6,7])
    testGraph2[3].extend([2,4,5])
    testGraph2[4].extend([1,3])
    
    testGraph3[0].extend([5,6,7])
    testGraph3[1].extend([1,3,5])
    testGraph3[2].extend([4,6])
    testGraph3[3].extend([5,6])
    testGraph3[4].extend([1,6,7])
    
    assert depthFirstSearch(testGraph1) == (1)
    
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    