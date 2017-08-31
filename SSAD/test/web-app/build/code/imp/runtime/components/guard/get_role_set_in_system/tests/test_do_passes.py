
import unittest
from runtime.objects.session.session import Session
from runtime.components.guard.get_role_set_in_system.tests.harness import TestHarness
from runtime.datatypes.cmd.cmd import Cmd

class TestDoPasses(TestHarness):

    def test_do_passes(self):
        print "test_do_passes"

        session = self.session

        instr = {'cmd': Cmd.get_role_set_in_system, 'session': session}

        guard = self.component
        result = guard.do(instr)

        self.assertEqual(result, instr)
