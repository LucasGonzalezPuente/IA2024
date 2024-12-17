import random
from graph1 import Graph
from node1 import Node
import networkx as nx




def main():
    
    problema=Graph()
    num_nodes = -1

    ##We ask for the number of nodes we want
    #while num_nodes != 0:
    
    num_nodes = int(input("How many nodes do you want? (Minimum of 5 please)-> "))
    if num_nodes < 5:
        print("Please , give a number greater/equal than 5")
        num_nodes = int(input("How many nodes do you want? (Minimum of 5 please)-> "))

        ##The number of edges depends on the number of nodes
    num_edges=-1
    if 4< num_nodes <= 7:
            num_edges=int((num_nodes*(num_nodes-1))/2)-3
    else:
            num_edges=int(num_nodes*random.uniform(1.5, 3))

    problema.creating_random_graph(num_nodes,num_edges)
    problema.draw()


if __name__ == "__main__":
    main()
 
