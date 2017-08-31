
import unittest
from runtime.objects.session.session import Session
from runtime.objects.email.email import Email
from runtime.objects.user.user import User
from runtime.objects.name.name import Name
from runtime.objects.role.role import Role
from runtime.components.engine.set_email.tests.harness import TestHarness
from runtime.datatypes.cmd.cmd import Cmd

class TestDoPasses(TestHarness):

    def test_do_passes(self):
        print "test_do_passes"
        session = self.session
        instr = {'cmd': Cmd.set_email, 
                 'session': session, 
                 'data': {'user': self.d_user,
                          'setemail': Email(val="duser@gnu.org")}
        }
        result_user = User(name=Name(val="user user"),
                           email=Email(val="duser@gnu.org"),
                           roles=[Role.user])
        engine = self.component
        result = engine.do(instr)
        print result
        self.assertEqual(result['result'], result_user)
