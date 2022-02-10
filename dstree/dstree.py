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


