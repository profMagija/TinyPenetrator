﻿
from .ExprNode import *
from .ASTNode import *
class GoToNode(ASTNode):
    """description of class"""
    def __init__(self, dest):
        self.dest = dest

