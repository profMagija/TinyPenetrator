﻿import unittest 

from ..parser.ast import *
from ..parser import *
from .. import *
class TestCodegen(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_let(self):
        code = LetNode("X", parse_expr(["3", "+", "Y"]))
        st = code.codegen()
        self.assertTrue('48' in st)
    
    def test_var(self):
        code = VarNode("B").codegen()
        self.assertEqual(len(code.split("\n")), 4)
        self.assertTrue("vars+2" in code)
    
    def test_num(self):
        code = NumNode(5).codegen()
        self.assertEqual(len(code.split("\n")), 4)
        self.assertTrue("HL,5" in code)

    def test_if(self):
        code = IfNode(NumNode(5), '>', NumNode(2), ReturnNode())
        st = code.codegen()
        self.assertEqual(1,1)

    def test_print(self):
        code = PrintNode([StrNode("hello world")]).codegen()
        self.assertEqual(len(code.split("\n")), 3)

        code = PrintNode([parse_expr(["2", "+", "3"])]).codegen()
        self.assertEqual(len(code.split("\n")), 16)

    def test_all(self):
        s = """
10 IF 1<2 THEN IF 2 < 3 THEN GOTO 10
        """
        s = do_all(s)
        pass

