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
            
            
if __name__ == "__main__":
    
    gGraph = defaultdict(list)
    
    gGraph[0].extend([1,2])
    gGraph[1].extend([0,3,4])
    gGraph[2].extend([0,3])
    gGraph[3].extend([1,2,4])
    gGraph[4].extend([1,3])
    
    depthFirstSearch(gGraph)