import math
import random
from queue import Queue
from node1 import Node

import networkx as nx  # biblioteca de tratamento de grafos necessária para desnhar graficamente o grafo
import matplotlib.pyplot as plt  # idem

# List with the possible names of the nodes
cities = [
    "Lisboa", "Oporto", "Coimbra", "Faro", "Funchal", "Angra do Heroísmo", "Ponta Delgada",
    "Luanda", "Benguela", "Lubango", "Huambo", "N'dalatando", "Maputo", "Beira", "Nampula",
    "Quelimane", "Tete", "Praia", "Mindelo", "Santa Catarina", "Assomada", "Bissau", "Bafatá",
    "Bolama", "Gabú", "Díli", "Baucau", "Same", "Maliana", "Aileu", "Rio de Janeiro", 
    "São Paulo", "Salvador", "Fortaleza", "Belo Horizonte", "Curitiba", "Recife", "Manaus", 
    "Belém", "Porto Alegre", "Goiânia", "Florianópolis", "Maceió", "Natal", "Vitória", 
    "Campo Grande", "São Luís", "João Pessoa", "Aracaju", "Palmas","Braga","Guimarães"
]

class Graph:  

    def __init__(self):
            self.m_nodes = []
            self.m_edges =[]
            self.m_graph = {} 
            self.m_h = {} 

    def __str__(self):
        out = ""
        for key in self.m_graph.keys():
            out += f"{key}: {self.m_graph[key]}\n"
            return out


    def add_edge(self, node1, node2, weight):
        n1 = Node(node1)
        n2 = Node(node2)
        if n1.getName() not in self.m_graph:
            self.m_nodes.append(n1)
            self.m_graph[n1.getName()] = []
        else:
            n1 = self.get_node_by_name(node1)

        if n2.getName() not in self.m_graph:
            self.m_nodes.append(n2)
            self.m_graph[n2.getName()] =[]
        else:
            n2 = self.get_node_by_name(node2)

        self.m_graph[n1.getName()].append((n2.getName(), weight))
        self.m_edges.append((node1,node2,weight))



    def get_node_by_name(self, name):
        for node in self.m_nodes:
                if node.getName() == name:
                    return node
        return None

     

    def creating_random_graph(self,num_nodos, num_aristas):
        #
        if num_nodos > len(cities):
            raise ValueError("No hay suficientes nombres de ciudades para el número de nodos solicitado.")
        
        #Selecting random names for nodes
        self.m_nodes = [Node(city) for city in random.sample(cities, num_nodos)]
        self.m_graph = {node.getName(): [] for node in self.m_nodes}


        
        #Adding nodes and edges
        for _ in range(num_aristas):
            # Chosing 2 nodes to connect
            node1, node2 = random.sample(self.m_nodes, 2)
            # Generate random weight
            weight = random.randint(10, 100)
            # add to the list
            self.add_edge(node1.getName(), node2.getName(), weight)

    #    return grafo



    def draw(self):
        g = nx.Graph()
        lista_v = self.m_nodes
        lista_a = []
        for node in lista_v:
            n = node.getName()
            g.add_node(n)
            for (adjacente, peso) in self.m_graph[n]:
                lista = (n, adjacente)
                #lista_a.append(lista)
                g.add_edge(n, adjacente, weight=peso)



        pos = nx.spring_layout(g)

        nx.draw_networkx_nodes(g, pos,node_size = 850,node_color='brown')
        nx.draw_networkx_labels(g,pos,font_size = 12,font_weight='bold')
        nx.draw_networkx_edges(g, pos, width=2)

        labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

        plt.title("Resulting Graph")
        plt.draw()
        plt.show()
