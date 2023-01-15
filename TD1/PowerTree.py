# -*- coding: utf-8 -*-

class PowerTree:
    def __init__(self): 
        self.layers=[[1]]
        self.parent={1:1}
    
    def draw_tree(self):
        for i in range(len(self.layers)):	
            print("layer",i)
            for j in self.layers[i]: print(j,"->",self.parent[j])  
  	
    def path_from_root(self,k):
        if k not in self.parent:
            return -1
        res = [k]
        while k != 1:
            k = self.parent[k]
            res.append(k)
        res.reverse()
        return res

    def add_layer(self):
        last_layer = self.layers[-1]
        new_layer = []
        for k in last_layer:
            path = self.path_from_root(k)
            path = [i + k for i in path]
            for i in path:
                if i not in self.parent:
                    self.parent[i] = k
                    new_layer.append(i)
        self.layers.append(new_layer)

# tree = PowerTree()
# for i in range(5):
#     tree.add_layer()
# tree.draw_tree()
