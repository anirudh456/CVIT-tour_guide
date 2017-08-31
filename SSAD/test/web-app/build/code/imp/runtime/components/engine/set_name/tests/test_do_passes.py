
import unittest
from runtime.objects.session.session import Session
from runtime.objects.name.name import Name
from runtime.objects.user.user import User
from runtime.objects.role.role import Role
from runtime.objects.email.email import Email
from runtime.components.engine.set_name.tests.harness import TestHarness
from runtime.datatypes.cmd.cmd import Cmd

class TestDoPasses(TestHarness):

    def test_do_passes(self):
        print "test_do_passes"
        session = self.session
        instr = {'cmd': Cmd.set_name, 
                 'session': session, 
                 'data': {'user': self.d_user,
                          'setname': Name(val="duser")}
        }

        result_user = User(name=Name(val="duser"),
                      email=Email(val="user@gnu.org"),
                      roles=[Role.user])
        engine = self.component
        result = engine.do(instr)
        self.assertEqual(result['result'], result_user)
