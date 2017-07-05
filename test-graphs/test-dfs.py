import networkx as nx
import pprint
import matplotlib.pyplot as plt
import numpy as np
import sys,time
from collections import deque


node_traversal_list = []    # global list to keep track of traversed nodes

###############################################################################
def dfs_r(n, G, goal):
    node_traversal_list.append(n)
    if n==goal: # base case 1
        return True
    else:
        children = G.successors(n)

        if len(children) == 0: # base case 2
            if(n == goal):
                return True
            else:
                return False
        else:

            for c in children:
                r = dfs_r(c,G,goal)
                if r == True:
                    return True

            return False



def bfs_i(root, G, goal):
    # create data structures
    S = set([])
    Q = deque([])

    # add to the set and queue
    S.add(root)
    Q.append(root)

    # iterate through adjacent nodes
    while(len(list(Q)) != 0):
        current = Q.popleft()
        node_traversal_list.append(current)
        if current == goal:
            return True
        else:
            neighbours = G.successors(current)

            for n in neighbours:
                if n not in S:
                    S.add(n)
                    Q.append(n)


###############################################################################


def randomise_tree(G):
    N = 2
    for i in range(N):

        # take a leaf and connect to another leaf
        leaf1 = np.random.choice([x for x in G.nodes_iter() if G.out_degree(x)==0])
        new_parent = np.random.choice([x for x in G.nodes_iter() if G.out_degree(x)==0 and x!=leaf1])
        print leaf1, new_parent
        parent = G.predecessors(leaf1)[0]
        #new_parent = np.random.choice([x for x in G.nodes_iter() if G.out_degree(x)==0 and x!=leaf1])

        # disconnect from old and connect to new
        G.remove_edge(parent,leaf1)
        G.add_edge(new_parent, leaf1)
        print len(G.edges())


    return G


def dump_graph(G):
    print "---"
    pprint.pprint(G.edges())
    print "---"
    print len(G.nodes())


def draw_graph(G, goal):
    plt.figure()
    cols = ['y'] * len(G.nodes())
    cols[goal] = 'r'
    plt.ion()
    nx.draw(G, with_labels=True, node_color=cols)



#SEED=123
SEED=int(time.time());
print "SEED=", SEED
N = 10

np.random.seed(SEED)
G = nx.balanced_tree(3,2, create_using=nx.DiGraph())
#G = randomise_tree(G) # optional
print "Total number of nodes = ", len(G.nodes())
#G = nx.gnp_random_graph(N,0.1, seed=SEED, directed=True)
#G = nx.random_tree(N)

goal = np.random.choice(G.nodes())
#root = np.random.choice(G.nodes()) # random root
root = 0

print "goal=", goal
#print "rand_root=", rand_root
draw_graph(G, goal)

node_traversal_list=[]
dfs_r(root, G, goal)
print "DFS - traversal distance = ", len(node_traversal_list), "; reached_goal=", node_traversal_list[-1]
print node_traversal_list

node_traversal_list=[]
bfs_i(root, G, goal)
print "BFS - traversal distance = ", len(node_traversal_list), "; reached_goal=", node_traversal_list[-1]
print node_traversal_list

plt.show()

x = raw_input('\nPress key to exit..\n')
