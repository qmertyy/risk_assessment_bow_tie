from gates import Gate

# define Python user-defined exceptions
class InvalidChildAmount(Exception):
    "you are trying to add another gate as child for a node that already is attached to a gate"
    pass

class Node:
    def __init__(self, name):
        self.name = name
        self.level = None
        self.probability = 0
        self.belongs_to = None
        self.parents = set()
        self.children = set()

    def add_child(self, child):
        assert isinstance(child, Gate), print('only gates can be a child for a node, see transfer gate')
        if len(self.children) == 1:
            gate_name_1 = list(self.children)[0].name.split('_')[1::]
            gate_name_2 = child.name.split('_')[1::]
            if gate_name_1 == gate_name_2:
                pass
            else:
                raise InvalidChildAmount
        self.children.add(child)      

    def add_parent(self, parent):
        assert isinstance(parent, Gate), print('only gates can be a parent for a node, see transfer gate')
        self.parents.add(parent)   

    def set_probability(self, prob):
        self.probability = prob
