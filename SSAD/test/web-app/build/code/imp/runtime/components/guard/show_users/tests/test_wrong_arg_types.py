
import unittest
from runtime.objects.session.session import Session
from runtime.components.guard.show_users.tests.harness import TestHarness
from runtime.datatypes.cmd.cmd import Cmd

class TestWrongArguments(TestHarness):

    def test_pass(self):
        print "test_with_wrong_type_arguments"

        session = self.session
        instr = {'cmd': Cmd.show_users, 'session': 'xyz'}
        guard = self.component
        with self.assertRaises(Exception):
            guard.do(instr)
