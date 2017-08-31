
import unittest
from runtime.objects.session.session import Session
from runtime.objects.role.role import Role
from runtime.components.guard.add_role.tests.harness import TestHarness
from runtime.datatypes.cmd.cmd import Cmd

class TestDoPasses(TestHarness):

    def test_do_passes(self):
        print "test_do_passes"
        
        # Current Session
        session = self.session
        n_user = User(name=Name(val="new user"),
                   email=Email(val="n@gnu.org"),
                   roles=[Role.user])

        
        instr = {
            'cmd': Cmd.add_role, 
            'session': session, 
            'data': {'user' : n_user,
                     'addrole': Role.user}
        }
        guard = self.component
        result = guard.do(instr)
        self.assertEqual(result, instr)
