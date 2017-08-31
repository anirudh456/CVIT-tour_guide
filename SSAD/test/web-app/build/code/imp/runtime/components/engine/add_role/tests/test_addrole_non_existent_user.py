
import unittest
from runtime.objects.session.session import Session
from runtime.objects.role.role import Role
from runtime.components.engine.add_role.tests.harness import TestHarness
from runtime.datatypes.cmd.cmd import Cmd

class TestDoPasses(TestHarness):

    def test_do_passes(self):
        print "test_do_passes"
        session = self.session
        self.component.em.delete_user(self.d_user)
        instr = {'cmd': Cmd.add_role, 
                 'session': session, 
                 'data': {'user': self.d_user,
                          'addrole': Role.admin}
}
        engine = self.component
        with self.assertRaises(Exception):
            engine.do(instr)
