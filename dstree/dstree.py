import os
import patlib

PIPE = "|"
ELBOW = "└──"
TEE   = "├──"
PIPE_PREFIX = "|   "
SPACE_PREFIX = "    "

class DirTree:
    def __init__(self,root_dir):
        self._generator = _TreeGenerator(root_dir)
    
    def generate(self):
        tree = self._generator.build_tree()
        for item in tree:
            print(item)


class _TreeGenerator():
    def __init__(self,root_dir):
        self._tree = []
        self._root_dir = patlib.Path(root_dir)
    
    def build_tree(self):
        self._tree_head()
        self._tree_body(self._root_dir)
        return self._tree
    
    
    
    
