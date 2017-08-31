
import unittest
from runtime.objects.session.session import Session
from runtime.components.guard.del_user.tests.harness import TestHarness
from runtime.datatypes.cmd.cmd import Cmd

class TestCannotDeleteOnself(TestHarness):

    def test_cannot_delete_oneself(self):
        print "test_cannot_delete_oneself"

        instr = {'cmd': Cmd.del_user, 
                 'session': self.session, 
                 'data': {'user': self.user}}

        guard = self.component
        with self.assertRaises(Exception):
            guard.do(instr)
