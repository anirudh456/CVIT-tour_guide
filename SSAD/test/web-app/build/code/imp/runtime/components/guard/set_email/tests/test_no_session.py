
import unittest
from runtime.objects.email.email import Email
from runtime.objects.session.session import Session
from runtime.components.guard.set_email.tests.harness import TestHarness
from runtime.datatypes.cmd.cmd import Cmd

class TestNoSession(TestHarness):

    def test_no_session(self):
        print "test_no_session"
        # delete session from entity manager setup in the TestHarness
        self.component.em.delete_session(self.session)
        session = self.session
        instr = {'cmd': Cmd.set_email, 
                 'session': session, 
                 'data': {'user': self.d_user,
                          'setemail': Email(val="duser@gnu.org")}
        }
        guard = self.component
        with self.assertRaises(Exception):
            guard.do(instr)
