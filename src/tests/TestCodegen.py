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
    
    def test_all(self):
        s = """
10 LET X = 3
20 LET Y = 5
30 IF X < Y THEN GOTO 10
40 RETURN
        """
        s = do_all(s)
        pass
