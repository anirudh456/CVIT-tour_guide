
import unittest
from unittest import TestCase
from runtime.objects.email.email import Email
from runtime.objects.name.name import Name
from runtime.objects.role.role import Role
from runtime.objects.user.user import User
from runtime.objects.session.session import Session
from runtime.datatypes.cmd.cmd import Cmd
from runtime.datatypes.instr.show_users.show_users_instr import ShowUsersInstr

class TestHarness(TestCase):
    def setUp(self):
        self.session = Session(user=User(email=Email(val="joe@g.com"), 
                                                                    name=Name(val="Joe Pesci"), 
                                                                    roles=[Role.admin]), 
                                                          role=Role.admin,
                                                          key="123")


    def tearDown(self):
      self.em = None

    def test_positive(self):
       instr = {'cmd': Cmd.show_users, 'session': self.session}
       self.assertTrue(ShowUsersInstr.is_inst(instr))


    def test_cmd_wrong(self):
       instr = {'cmd': "foo", 'session': self.session}
       self.assertFalse(ShowUsersInstr.is_inst(instr))


    def test_session_missing(self):
       instr = {'cmd': Cmd.show_users}
       self.assertFalse(ShowUsersInstr.is_inst(instr))


    def test_cmd_missing(self):
       instr = {'session': self.session}
       self.assertFalse(ShowUsersInstr.is_inst(instr))
