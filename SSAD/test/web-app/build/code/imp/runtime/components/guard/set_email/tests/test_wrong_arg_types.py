
import unittest
from runtime.objects.session.session import Session
from runtime.objects.email import Email
from runtime.components.guard.set_email.tests.harness import TestHarness
from runtime.datatypes.cmd.cmd import Cmd

class TestWrongArguments(TestHarness):

    def test_pass(self):
        print "test_with_wrong_type_arguments"

        session = self.session
        instr = {'cmd': Cmd.set_email, 
                 'session': 'session', 
                 'user': self.d_user}
        guard = self.component
        with self.assertRaises(Exception):
            guard.do(instr)
