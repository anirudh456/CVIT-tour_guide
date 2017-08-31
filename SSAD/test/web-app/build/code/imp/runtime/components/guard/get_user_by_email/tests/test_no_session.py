
import unittest
from runtime.objects.session.session import Session
from runtime.objects.email.email import Email
from runtime.components.guard.get_user_by_email.tests.harness import TestHarness
from runtime.datatypes.cmd.cmd import Cmd

class TestNoSession(TestHarness):

    def test_no_session(self):
        print "test_no_session"
        # delete session from entity manager setup in the TestHarness
        self.component.em.delete_session(self.session)
        session = self.session
        email = Email(val="user@gnu.org")
        instr = {'cmd': Cmd.get_user_by_email, 'session': session , 'data' : {'email':email}}
        guard = self.component
        with self.assertRaises(Exception):
            guard.do(instr)
