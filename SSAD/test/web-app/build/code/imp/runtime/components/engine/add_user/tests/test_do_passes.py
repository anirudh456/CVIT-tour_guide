
import unittest
from runtime.objects.session.session import Session
from runtime.components.engine.add_user.tests.harness import TestHarness
from runtime.datatypes.cmd.cmd import Cmd
from runtime.objects.email.email import Email
from runtime.objects.name.name import Name
from runtime.objects.role.role import Role
from runtime.objects.user.user import User

class TestDoPasses(TestHarness):

    def test_do_passes(self):
        print "test_do_passes"

        newUser = User(
            name=Name(val="New Name"),
            email=Email(val="n@g.c"),
            roles=[Role.admin]
        )

        session = self.session
        instr = {
            'cmd': Cmd.add_user, 
            'session': session,
            'data': {
                'user': newUser,
            }
        }
        engine = self.component
        result = engine.do(instr)
        print result
        self.assertEqual(result['instr'], instr)
        self.assertEqual(result['result'], newUser)
