
import unittest
from runtime.objects.user.user import User
from runtime.objects.session.session import Session
from runtime.objects.email.email import Email
from runtime.objects.name.name import Name
from runtime.objects.role.role import Role
from runtime.exceptions.app.exception import AppException
from runtime.exceptions.arity.exception import ArityException
from runtime.exceptions.keymismatch.exception import KeyMismatchException
from runtime.components.guard.del_role.tests.harness import TestHarness
from runtime.datatypes.cmd.cmd import Cmd

class TestCheckAuth(TestHarness):

    def test_check_auth(self):
        print "test_check_auth"
        session = self.session
        session = Session(user=self.d_user, role=Role.user, key="12345689")
        self.component.em.add_session(session)
        
        
        n_user = User(name=Name(val="new user"),
                      email=Email(val="n@gnu.org"),
                      roles=[Role.user,Role.admin])
        

        self.component.em.add_user(n_user)

        instr = {'cmd': Cmd.add_role, 
                 'session': session, 
                 'data': {'user': n_user,
                          'delrole': Role.user}
        }

        guard = self.component
        with self.assertRaises(Exception):
            guard.do(instr)
