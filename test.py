# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 09:25:37 2017

@author: Vy
"""

import unittest
from way import *


class Test_WAY(unittest.TestCase):
    """Test WAY modules introspection capabilieties"""
    def setUp(self):
        class A:
            def __init__(self, arg_one,  arg_two):
                self.arg_one = arg_one
                self.arg_two = arg_two
            def printer(self):
                print(self.arg_one, self.arg_two)   
        class B:
            def __init__(self, arg_three,  arg_four, arg_one):
                self.arg_three = arg_three
                self.arg_four =  arg_four
                # Adding overlaping argument with A object
                # In different position                
                self.arg_one = arg_one
            def printer(self):
                print(self.arg_three, self.arg_four, self.arg_one)
                
        def test_function(arg_one):
            """Test function"""
            print(arg_one)
            
        self.example_with_string = "Variable example"
        self.example_with_integer = 5 # Example with int
        self.B = B("three", "four", "one")
        self.introspec_obj_a = WAY(A("one", "two"))
        self.introspec_obj_b = WAY(B("three", "four", "one"))
        self.introspec_function = WAY(test_function("test"))

    def test_WIYN(self):
        """Tests the objects name"""
        self.assertEqual(self.introspec_obj_a.WIYN(), "A")
        self.assertEqual(self.introspec_obj_b.WIYN(), "B")
        self.assertEqual(self.introspec_function.WIYN(), "introspec_function")
        
        
if __name__=="__main__":
    unittest.main()
            
        