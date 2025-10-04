# -*- coding: utf-8 -*-
""" 
Created on Sat Oct 4 21:13:22 2025
@author:  Saptarshi
 """
from volume_cuboid import *
import unittest

# Test1
class TestCuboid(unittest.TestCase):
  def test_volume(self):
    self.assertAlmostEqual(cuboid_volume(2), 8)
    self.assertAlmostEqual(cuboid_volume(1), 1)
    self.assertAlmostEqual(cuboid_volume(0), 0)
  def test_input_value(self):
    self.assertRaises(TypeError, cuboid_volume, True)
    