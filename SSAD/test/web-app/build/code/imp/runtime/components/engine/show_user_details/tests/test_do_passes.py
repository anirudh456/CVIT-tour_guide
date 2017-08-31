
import unittest
from runtime.objects.session.session import Session
from runtime.objects.email.email import Email
from runtime.objects.user.user import User
from runtime.objects.name.name import Name
from runtime.objects.role.role import Role
from runtime.components.engine.show_user_details.tests.harness import TestHarness
from runtime.datatypes.cmd.cmd import Cmd

class TestDoPasses(TestHarness):

    def test_do_passes(self):
        print "test_do_passes"
        session = self.session
        instr = {'cmd': Cmd.show_user_details, 
                 'session': session, 
                 'data': {'email':Email(val="user@gnu.org")}
        }

        result_dict= {'roles_of_user':[Role.user,Role.admin],
                      'name_of_user':"user user",
                      'email_of_user':"user@gnu.org"}
        engine = self.component
        result = engine.do(instr)
        self.assertEqual(result['result'], result_dict)
