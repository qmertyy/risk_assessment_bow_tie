'''This event tree module uses draw io dagrams to recreate event paths. qmerty'''

import xml.etree.ElementTree as ET
import base64
import zlib
from collections import defaultdict
from urllib.parse import unquote

class EventTree():
    def __init__(self, outcomes, path_to_diagram):
        
        self.outcomes = outcomes # collision or no collision
        self.path_to_diagram = path_to_diagram

        # create the Element Tree 
        tree = ET.parse(self.path_to_diagram)
        root = tree.getroot()
        data = base64.b64decode(tree.find('diagram').text)
        xml = zlib.decompress(data, wbits=-15)
        xml = unquote(xml)
        self.event_tree = ET.fromstring(xml)   

    '''  def reconstruct_path(self, id, tree, constructed_path = []):           
        search_query = f".//mxCell[@target='{id}']"  
        for cell_t in tree.findall(search_query):
                new_id = cell_t.get('source')
                new_query =  f".//mxCell[@id='{new_id}']"
                for cell_b in tree.findall(new_query):  
                    #print(cell_b.items())              
                    constructed_path.append(cell_b.get('value'))           
                    constructed_path = self.reconstruct_path(cell_b.get('id'), tree, constructed_path)
                
        
        return constructed_path'''

    def reconstruct_path(self, id, tree, paths=None):
        if paths is None:
            paths = []           
        search_query = f".//mxCell[@target='{id}']"       
        for cell_t in tree.findall(search_query):
                new_id = cell_t.get('source')
                new_query =  f".//mxCell[@id='{new_id}']"
                for cell_b in tree.findall(new_query):                                
                    paths.append(cell_b.get('value'))           
                    paths = self.reconstruct_path(cell_b.get('id'), tree, paths)
        return paths
    def build(self):
        reconstructed_paths = []
        final_paths = defaultdict(list)
        for cell in self.event_tree.iter('mxCell'):    
            cell_name = cell.get('value')
            if cell_name in self.outcomes:                    
                constructed_path = self.reconstruct_path(cell.get('id'), self.event_tree)
                constructed_path = constructed_path[::-1]
                constructed_path.append(cell_name)
                reconstructed_paths.append(constructed_path)
        for idx, pth in enumerate(reconstructed_paths):
            final_paths[idx] = pth
        return final_paths

