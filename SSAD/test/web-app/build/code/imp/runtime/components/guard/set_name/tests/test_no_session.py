
import unittest
from runtime.objects.name.name import Name
from runtime.objects.session.session import Session
from runtime.components.guard.set_name.tests.harness import TestHarness
from runtime.datatypes.cmd.cmd import Cmd

class TestNoSession(TestHarness):

    def test_no_session(self):
        print "test_no_session"
        # delete session from entity manager setup in the TestHarness
        self.component.em.delete_session(self.session)
        session = self.session
        instr = {'cmd': Cmd.set_name, 
                 'session': session, 
                 'data': {'user': self.d_user,
                          'setname': Name(val="duser")}
        }
        guard = self.component
        with self.assertRaises(Exception):
            guard.do(instr)
