
import unittest
from runtime.objects.session.session import Session
from runtime.objects.name.name import Name
from runtime.components.guard.set_name.tests.harness import TestHarness
from runtime.datatypes.cmd.cmd import Cmd

class TestDoPasses(TestHarness):

    def test_do_passes(self):
        print "test_do_passes"
        session = self.session
        instr = {'cmd': Cmd.set_name, 
                 'session': session, 
                 'data': {'user': self.d_user,
                          'setname': Name(val="duser")}
        }
        guard = self.component
        result = guard.do(instr)
        self.assertEqual(result, instr)
