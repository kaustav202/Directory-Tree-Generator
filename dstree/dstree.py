import os
import pathlib

PIPE = "|"
ELBOW = "└──"
TEE   = "├──"
PIPE_PREFIX = "|   "
SPACE_PREFIX = "    "

class DirTree:
    def __init__(self,root_dir):
        self._generator = _TreeGenerator(root_dir) #Composition
    
    def generate(self):
        tree = self._generator.build_tree()
        for item in tree:
            print(item)


class _TreeGenerator():
    def __init__(self,root_dir):
        self._tree = []
        self._root_dir = pathlib.Path(root_dir)
    
    def build_tree(self):
        self._tree_head()
        self._tree_body(self._root_dir)
        return self._tree
    
    def _tree_head(self):
        self._tree.append(f"{self._root_dir}{os.sep}")
        self._tree.append(PIPE)

    def _tree_body(self,directory,prefix = ""):
        entries = directory.iterdir()
        entries = sorted(entries, key = lambda x : x.is_file())
        entry_count = len(entries)
        for index,entry in enumerate(entries):
            connector = ELBOW if index == entry_count-1 else TEE
            if entry.is_dir():
                self._add_directory(entry,index,entry_count,prefix,connector)
            else:
                self._add_file(entry,prefix,connector)
    
    
    
