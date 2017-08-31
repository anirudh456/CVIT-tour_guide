
import unittest
from runtime.objects.session.session import Session
from runtime.objects.email.email import Email
from runtime.components.guard.set_email.tests.harness import TestHarness
from runtime.datatypes.cmd.cmd import Cmd

class TestDoPasses(TestHarness):

    def test_do_passes(self):
        print "test_do_passes"
        session = self.session
        instr = {'cmd': Cmd.set_email, 
                 'session': session, 
                 'data': {'user': self.d_user,
                          'setemail': Email(val="duser@gnu.org")}
        }
        guard = self.component
        result = guard.do(instr)
        self.assertEqual(result, instr)
