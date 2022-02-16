import pathlib
import argparse
import sys

from . import __version__
from .dstree import DirTree

def main():
    args = parse_args()
    root_dir = pathlib.Path(args.root_dir)
    if not root_dir.is_dir():
        print("Entered directory is invalid!! ")
        sys.exit()
    tree = DirTree(root_dir)
    tree.generate()

