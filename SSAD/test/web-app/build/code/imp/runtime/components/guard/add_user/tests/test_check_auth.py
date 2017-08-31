
import unittest
from runtime.objects.user.user import User
from runtime.objects.session.session import Session
from runtime.objects.email.email import Email
from runtime.objects.name.name import Name
from runtime.objects.role.role import Role
from runtime.exceptions.app.exception import AppException
from runtime.exceptions.arity.exception import ArityException
from runtime.exceptions.keymismatch.exception import KeyMismatchException
from runtime.components.guard.add_user.tests.harness import TestHarness
from runtime.datatypes.cmd.cmd import Cmd

class TestCheckAuth(TestHarness):

    def test_check_auth(self):
        print "test_check_auth"

        user = User(
            name=Name(val="Hey Name"),
            email=Email(val="h@g.c"),
            roles=[Role.user]
        )
          
        self.component.em.add_user(user)

        # New Session
        session = Session(user=user, role=Role.user, key="asdfdssdf")

        self.component.em.add_session(session)

        newUser = User(
            name=Name(val="A new User"), 
            email=Email(val="new.user@something.com"),
            roles=[Role.user]
        )
        
        instr = {
            'cmd': Cmd.add_user, 
            'session': session, 
            'data': {
                'user' : newUser
            }
        }

        guard = self.component

        with self.assertRaises(AppException):
            result = guard.do(instr)
              
