﻿import ExprNode
import ASTNode
class LetNode(ASTNode):
    """represents a LET <var> = <expr> statement"""
    def __init__(self:LetNode, var: str, expr: ExprNode):
        self.var = var
        self.expr = expr

