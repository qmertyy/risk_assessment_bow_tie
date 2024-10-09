

class Gate():
    def __init__(self, name, gate_type):   
        assert gate_type in ['transfer', 'and', 'or'], print('gate types can only be transfer, or / and')     
        self.name = name   
        self.gate_type = gate_type
        self.children = set()
        self.parents = set()
        self.probability = 0         
    def add_child(self, child):
        self.children.add(child)
    def add_parent(self, parent):
        self.parents.add(parent)
    def update_probability(self):
        if self.gate_type == 'and':
            self.probability = 1
            for input_node in self.children:
                self.probability *= input_node.probability 
        elif self.gate_type == 'or':
            self.probability = 0
            for input_node in self.children:
                self.probability += input_node.probability - (input_node.probability * self.probability)
    def set_probability(self, probability):
        self.probability = probability