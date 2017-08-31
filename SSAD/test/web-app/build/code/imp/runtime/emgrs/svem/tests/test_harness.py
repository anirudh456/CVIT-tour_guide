
import unittest
from unittest import TestCase
from runtime.emgrs.svem.svem import EntityMgr

class TestHarness(TestCase):
    def setUp(self):
      self.em = EntityMgr()

    def tearDown(self):
      self.em = None
