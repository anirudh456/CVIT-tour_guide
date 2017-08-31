
import unittest
from runtime.objects.session.session import Session
from runtime.objects.email.email import Email
from runtime.components.guard.get_user_by_email.tests.harness import TestHarness
from runtime.datatypes.cmd.cmd import Cmd

class TestDoPasses(TestHarness):

    def test_do_passes(self):
        print "test_do_passes"
        session = self.session
        email = Email(val = "user@gnu.org")
        instr = {'cmd': Cmd.get_user_by_email, 'session': session, 'data': {'email' : email}}
        guard = self.component
        result = guard.do(instr)
        self.assertEqual(result, instr)
