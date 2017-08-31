
import unittest
from runtime.objects.session.session import Session
from runtime.components.guard.get_user_by_email.tests.harness import TestHarness
from runtime.datatypes.cmd.cmd import Cmd

class TestWrongArguments(TestHarness):

    def test_pass(self):
        print "test_with_wrong_type_arguments"

        session = self.session
        instr = {'cmd': Cmd.get_user_by_email, 'session': 'xyz'}
        guard = self.component
        with self.assertRaises(Exception):
            guard.do(instr)
