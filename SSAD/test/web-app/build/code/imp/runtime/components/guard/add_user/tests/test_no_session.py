
import unittest
from runtime.objects.session.session import Session
from runtime.objects.role.role import Role
from runtime.objects.name.name import Name
from runtime.objects.email.email import Email
from runtime.objects.user.user import User
from runtime.exceptions.app.exception import AppException
from runtime.exceptions.arity.exception import ArityException
from runtime.exceptions.keymismatch.exception import KeyMismatchException
from runtime.components.guard.add_user.tests.harness import TestHarness
from runtime.datatypes.cmd.cmd import Cmd

class TestNoSession(TestHarness):

    def test_no_session(self):
        print "test_no_session"
        # delete session from entity manager setup in the TestHarness
        self.component.em.delete_session(self.session)
        session = self.session
        user = User(
            name=Name(val="Jon doe"),
            email=Email(val="jon@doe.co"),
            roles=[Role.user]
        )
        instr = {
            'cmd': Cmd.add_user, 
            'session': session, 
            'data': {
                'user': user
            }
        }
        guard = self.component
        with self.assertRaises(AppException):
            guard.do(instr)
