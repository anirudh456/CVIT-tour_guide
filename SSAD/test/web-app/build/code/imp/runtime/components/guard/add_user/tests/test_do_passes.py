
import unittest
from runtime.objects.user.user import User
from runtime.objects.email.email import Email
from runtime.objects.name.name import Name
from runtime.objects.role.role import Role
from runtime.exceptions.app.exception import AppException
from runtime.exceptions.arity.exception import ArityException
from runtime.exceptions.keymismatch.exception import KeyMismatchException
from runtime.components.guard.add_user.tests.harness import TestHarness
from runtime.datatypes.cmd.cmd import Cmd

class TestDoPasses(TestHarness):

    def test_do_passes(self):
        print "test_do_passes"
        
        # Current Session
        session = self.session

        user = User(
            name=Name(val="A new User"), 
            email=Email(val="new.user@something.com"),
            roles=[Role.user]
        )
        
        instr = {
            'cmd': Cmd.add_user, 
            'session': session, 
            'data': {
                'user' : user
            }
        }
        guard = self.component
        result = guard.do(instr)
        self.assertEqual(result, instr)
