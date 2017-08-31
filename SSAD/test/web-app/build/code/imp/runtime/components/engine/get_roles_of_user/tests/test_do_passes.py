
import unittest
from runtime.objects.email.email import Email
from runtime.objects.name.name import Name
from runtime.objects.role.role import Role
from runtime.objects.user.user import User
from runtime.objects.session.session import Session
from runtime.components.engine.get_roles_of_user.tests.harness import TestHarness
from runtime.datatypes.cmd.cmd import Cmd

class TestDoPasses(TestHarness):

    def test_do_passes(self):
        print "test_do_passes"
        session = self.session
        instr = {'cmd': Cmd.get_roles_of_user, 
                 'session': session, 
                 'data': {'user': self.d_user}
        }

        result_roles =[Role.user,Role.admin]
        engine = self.component
        result = engine.do(instr)
        self.assertEqual(result['result'], result_roles)
