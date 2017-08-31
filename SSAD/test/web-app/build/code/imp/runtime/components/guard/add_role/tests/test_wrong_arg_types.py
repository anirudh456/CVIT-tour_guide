
import unittest
from runtime.objects.session.session import Session
from runtime.objects.role.role import Role
from runtime.components.guard.add_role.tests.harness import TestHarness
from runtime.datatypes.cmd.cmd import Cmd

class TestWrongArguments(TestHarness):

    def test_pass(self):
        print "test_with_wrong_type_arguments"

        session = self.session
        instr = {'cmd': Cmd.add_role, 
                 'session': 'session', 
                 'user': self.d_user}
        guard = self.component
        with self.assertRaises(Exception):
            guard.do(instr)
