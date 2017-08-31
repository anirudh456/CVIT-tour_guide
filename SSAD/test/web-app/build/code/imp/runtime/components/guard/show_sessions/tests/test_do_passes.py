
import unittest
from runtime.objects.session.session import Session
from runtime.components.guard.show_sessions.tests.harness import TestHarness
from runtime.datatypes.cmd.cmd import Cmd

class TestDoPasses(TestHarness):

    def test_do_passes(self):
        print "test_do_passes"
        session = self.session
        instr = {'cmd': Cmd.show_sessions, 'session': session}
        guard = self.component
        result = guard.do(instr)
        print result
        self.assertEqual(result, instr)
