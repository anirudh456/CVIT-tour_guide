
import unittest
from runtime.objects.role.role import Role
from runtime.objects.session.session import Session
from runtime.components.engine.get_role_set_in_system.tests.harness import TestHarness
from runtime.datatypes.cmd.cmd import Cmd

class TestDoPasses(TestHarness):

    def test_do_passes(self):
        print "test_do_passes"
        session = self.session
        instr = {'cmd': Cmd.get_role_set_in_system, 
                 'session': session
        }
        engine = self.component
        result = engine.do(instr)
        self.assertEqual(result['result'],[Role.admin,Role.user])
