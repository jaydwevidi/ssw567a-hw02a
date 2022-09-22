# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangleA(self):
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testInvalidTriangleA(self):
        self.assertEqual(classifyTriangle(1, 2, 5), 'NotATriangle', '1,2,5 is not a triangle')

    def testInvalidTriangleB(self):
        self.assertEqual(classifyTriangle(2, 2, 5), 'NotATriangle', '2,2,5 is not a triangle')

    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(5, 2, 4), 'Scalene', '5,2,4 is a Right triangle')

    def testEquilateralTriangleC(self):
        self.assertEqual(classifyTriangle(4, 4, 4), 'Equilateral', '4,4,4 should be equilateral')

    def testInvalidInteger(self):
        self.assertEqual(classifyTriangle(4, "four", 4), 'InvalidInput', 'a string value cannot be accepted')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

