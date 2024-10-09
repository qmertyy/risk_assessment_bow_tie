from nodes import Node
from gates import Gate
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt


class FaultTree:
    def __init__(self, name, my_tree, base_event_probs, transfer_event_probs, root_event):
        
        #  - Create the tree
        self.my_tree = my_tree  # my tree is a dictionary element that defines the structure of the tree
        node_set = set()
        gate_set = set()
        for key, structure in my_tree.items():
            # structure is a set (root, [], gate )
            root = structure[0]
            children = structure[1]
            gate = structure[2]
            for child in children:
                node_set.add(child)
            node_set.add(root)  #  example ---> ais_failure
            gate_set.add(gate+'_'+root)  #  example ---> or_ais_failure_tree
        

        # create node and gate dicts
        self.nodes, self.gates = defaultdict(Node), defaultdict(Gate)
        for no in node_set:
            self.nodes[no] = Node(no)
        for ga in gate_set:
            self.gates[ga] = Gate(ga, ga.split('_')[0])

        # define relations between parts
        for key, structure in my_tree.items():
            ''' key is tree name
                structure is the relationship'''
            root = structure[0]
            children = structure[1]
            gate = structure[2]
            gate_name = gate+'_'+root
            for child in children:  # all children will be connected to a parent gate               
                self.nodes[child].add_parent(self.gates[gate_name])       
                self.gates[gate_name].add_child(self.nodes[child])     
            self.nodes[root].add_child(self.gates[gate_name])  # root node will have the gate as the child
            self.gates[gate_name].add_parent(self.nodes[root])   
      
        #  - define remaining attributes
        self.name = name
        self.base_event_probs = base_event_probs  # this is a dictionary holding base event probabilities (probabilities for nodes without a child gate))
        self.transfer_event_probs = transfer_event_probs
        self.graph = nx.DiGraph(name=name) 
        self.root_event = root_event

        # -  calculate probabilities of each element and connect the tree
        self.calculate_probabilities()
        self.connect_tree()
        self.update_graph_probabilities()  # New method call
      
    def connect_tree(self,):
        for ga in self.gates.values():
            self.graph.add_node(ga, name= ga.name, color ='red')  
        for no in self.nodes.values():
            self.graph.add_node(no, name= no.name)
        for no in self.nodes.values():
            for child in no.children:
                # adds and edge between node and gate, multiple nodes can connect to a single child 
                self.graph.add_edge(child, no)    
            for parent in no.parents:
                # adds and edge between node and gate, multiple nodes can connect to a single child 
                self.graph.add_edge(no, parent)  

    def update_graph_probabilities(self):
        for node in self.graph.nodes():
            if isinstance(node, Node):
                self.graph.nodes[node]['probability'] = node.probability
            elif isinstance(node, Gate):
                self.graph.nodes[node]['probability'] = node.probability

    


    def update_nodes(self,ga):
        for _, no in self.nodes.items():
            try:
                if next(iter(no.children)).name == ga.name:
                    no.probability = ga.probability
            except StopIteration:
                pass
            
    def calculate_probabilities(self,):
        '''
            nodes get their probability for child gate,
            if a node doesnt have a child gate, probability comes from base_event_probs,
            if a node has a transfer gate as child, node probability comes from transfore_event_probs
        '''

        for key, no in self.nodes.items():
            try:
                gat = next(iter(no.children))
                if isinstance(gat, Gate):  
                    if gat.gate_type == 'transfer':                 
                            no.probability = self.transfer_event_probs[no.name] 
                            self.gates['transfer'+'_'+no.name].name = 'transfer'+'_'+no.name                     
                            self.gates['transfer'+'_'+no.name].probability = no.probability # they are assigned 0 if they are not calculated yet
                       
            except StopIteration:
                no.probability =  self.base_event_probs[no.name]               
            self.nodes[key] = no  
                    
            
        
        #  - at this point all the unknown events are gotten from the dictionaries and errors are thrown if the keys are not in the base or transfer event dicts

        gate_found = [True for _ in self.gates.values()]          
        while sum(gate_found) != 0:       # infinite loop iif there is a issue with fault tree creations
            for idx, _ in enumerate(gate_found):
                ga = list(self.gates.values())[idx]
                probs_children = [child.probability for child in ga.children if child.probability != 0]       
                if len(probs_children) == len(ga.children):       # check if all the child nodes have a probability calculated, transfer nodes may have 0 incase their time to be calculated is not there yet           
                    #  every child has a probability found earlier                  
                    ga.update_probability()  
                    self.update_nodes(ga)        
                    gate_found[idx] = False
                else:

                    pass                
            #print(f'calculated number of the gates is {len(gate_found)-sum(gate_found)}')
        #print('all the gate probabilities have been calculated, updating node probabilities accordingly')

        # update top node
        for _, no in self.nodes.items():
            if no.probability == 0 :               
                no.probability = next(iter(no.children)).probability
        #print('all node probabilities have been calculated')



                
            
                                 
    
                
           
                

        

    