
import unittest
from runtime.objects.session.session import Session
from runtime.objects.email.email import Email
from runtime.components.guard.ShowDetails.tests.harness import TestHarness
from runtime.datatypes.cmd.cmd import Cmd

class TestDoPasses(TestHarness):

    def test_do_passes(self):
        print "test_do_passes"
        session = self.session
        email = Email(val = "nouser@gnu.org")
        instr = {'cmd': Cmd.show_user_details, 'session': session, 'data': {'email' : email}}
        guard = self.component
        result = guard.do(instr)
        print result
        self.assertEqual(result, instr)
