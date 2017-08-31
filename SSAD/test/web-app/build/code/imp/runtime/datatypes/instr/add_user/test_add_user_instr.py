
import unittest
from unittest import TestCase
from runtime.objects.email.email import Email
from runtime.objects.name.name import Name
from runtime.objects.role.role import Role
from runtime.objects.user.user import User
from runtime.objects.session.session import Session
from runtime.datatypes.cmd.cmd import Cmd
from runtime.datatypes.instr.add_user.add_user_instr import AddUserInstr

class TestHarness(TestCase):
    def setUp(self):
        self.u1 = User(
            email=Email(val="joe@g.com"),
            name=Name(val="Joe Pesci"), 
            roles=[Role.admin])

        self.session = Session(
            user=self.u1,
            role=Role.admin,
            key="123")


    def tearDown(self):
      self.em = None

    def test_positive(self):
       instr = {'cmd': Cmd.add_user, 
                'session': self.session, 
                'data': {'user': self.u1}}
       self.assertTrue(AddUserInstr.is_inst(instr))


    def test_cmd_wrong(self):
       instr = {'cmd': Cmd.del_user, 'session': self.session}
       self.assertFalse(AddUserInstr.is_inst(instr))


    def test_session_missing(self):
       instr = {'cmd': Cmd.show_users}
       self.assertFalse(AddUserInstr.is_inst(instr))


    def test_cmd_missing(self):
       instr = {'session': self.session}
       self.assertFalse(AddUserInstr.is_inst(instr))
