'''RCM CLASS 
----> can change fault tree structure
----> can provide many variables 
----> calculates collision and foundering probability

RCO class
list of RCMS 

Example RCM

rcm_gps_failure = 
                    ('gps_sensory_duplication', 
                    effected_tree_name = 'base_gps_failure' ,
                    ,addt_base_trees = [], 
                    addt_bzero_tree= [], 
                    effected_base_prob = ('effect_node_name' , new_prob))
                    '''

import numpy as np
from utils.existing_trees import base_trees, bzero_trees
from collections import defaultdict
import json
import pickle
from utils.fault_tree import FaultTree


class RCM():
    def __init__(self, name, effected_tree_name = None, addt_trees = [], new_trees = [], effected_base_prob = []):
        '''Effected base prob = ('name', probability)'''

        # Variables
        self.name = name
        self.effected_tree_name = effected_tree_name
        self.addt_trees = addt_trees
        self.new_trees = new_trees
        self.effected_base_prob = effected_base_prob
        self.base_trees = base_trees()        
        self.bzero_trees = bzero_trees()


        # Load FSA 2nd step results
        f = open('./data/jsons/base_probabilities.json')
        
        self.base_event_probs = json.load(f)
        f.close()
        f = open('./data/jsons/transfer_events_probs.json')
      
        self.transfer_event_probs = json.load(f)
        f.close()

    def get_random_probs_in_range(self, start, stop, size):
        return np.random.uniform(start, stop, size)
    
    def implement(self):
        if self.effected_tree_name is not None:
           
            pointing_to = self.effected_tree_name.split('_')[0]
          
            # update trees
            if pointing_to == 'bzero':
                for tree in self.addt_trees:
                    temp_tree = getattr(self.bzero_trees, self.effected_tree_name)
                    print(tree)
                    temp_tree.update(tree)

                    setattr(self.bzero_trees, self.effected_tree_name, temp_tree)
                
            if pointing_to == 'base':
                for tree in self.addt_trees:
                    temp_tree = getattr(self.base_trees, self.effected_tree_name)                    
                    temp_tree.update(tree)                    
                    setattr(self.base_trees, self.effected_tree_name, tree)
                  

            if self.new_trees:
        
                for tree_struct in self.new_trees:
                    if tree_struct[0] == 'base':
                        tree_name = tree_struct[1]['tree1'][0]                        
                        setattr(self.base_trees, tree_name+'_tree', tree_struct[1])
                        
                      
                    if tree_struct[0] == 'bzero':
                      
                        tree_name = tree_struct[1]['tree1'][0]
                        setattr(self.bzero_trees, tree_name+'_tree', tree_struct[1])

       
        if self.effected_base_prob: # this one updates an already existing base probability
            
           
            for prob_update in self.effected_base_prob:
            
                if prob_update[0] == 'base':        
                    self.base_event_probs[prob_update[1][0]] = prob_update[1][1]
                   
                if prob_update[0] == 'transfer':
                    self.transfer_event_probs[prob_update[1][0]] = prob_update[1][1]
          

        
        return self.base_trees, self.bzero_trees, self.base_event_probs, self.transfer_event_probs




    


  
