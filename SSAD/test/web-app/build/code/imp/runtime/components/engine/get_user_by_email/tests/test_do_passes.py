
import unittest
from runtime.objects.email.email import Email
from runtime.objects.name.name import Name
from runtime.objects.role.role import Role
from runtime.objects.user.user import User
from runtime.objects.session.session import Session
from runtime.components.engine.get_user_by_email.tests.harness import TestHarness
from runtime.datatypes.cmd.cmd import Cmd

class TestDoPasses(TestHarness):

    def test_do_passes(self):
        print "test_do_passes"
        session = self.session
        instr = {'cmd': Cmd.get_user_by_email, 
                 'session': session, 
                 'data': {'email':Email(val="user@gnu.org")}
        }

        result_user= User(name=Name(val="user user"),
                          email=Email(val="user@gnu.org"),
                          roles=[Role.user,Role.admin])
        engine = self.component
        result = engine.do(instr)
        self.assertEqual(result['result'], result_user)
