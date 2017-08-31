
import unittest
from runtime.objects.session.session import Session
from runtime.components.engine.del_user.tests.harness import TestHarness
from runtime.datatypes.cmd.cmd import Cmd

class TestDoPasses(TestHarness):

    def test_do_passes(self):
        print "test_do_passes"
        session = self.session
        self.component.em.delete_user(self.d_user)
        instr = {'cmd': Cmd.del_user, 
                 'session': session, 
                 'data': {'user': self.d_user}}
        engine = self.component
        with self.assertRaises(Exception):
            engine.do(instr)
