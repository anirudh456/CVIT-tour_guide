
import unittest
from runtime.objects.role.role import Role
from runtime.objects.session.session import Session
from runtime.components.engine.del_role.tests.harness import TestHarness
from runtime.datatypes.cmd.cmd import Cmd

class TestDoPasses(TestHarness):

    def test_do_passes(self):
        print "test_do_passes"
        session = self.session
        instr = {'cmd': Cmd.del_role, 
                 'session': session, 
                 'data': {'user': self.d_user,
                          'delrole': Role.admin}
        }
        engine = self.component
        result = engine.do(instr)
        self.assertEqual(result['result'], [Role.user])
