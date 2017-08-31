
import unittest
from unittest import TestCase
from runtime.components.guard.guard import Guard
from runtime.components.guard.del_user.del_user import DelUser
from runtime.emgrs.svem.svem import EntityMgr
from runtime.objects.email.email import Email
from runtime.objects.name.name import Name
from runtime.objects.role.role import Role
from runtime.objects.user.user import User
from runtime.objects.session.session import Session
from runtime.datatypes.cmd.cmd import Cmd

class TestHarness(TestCase):
    TESTING = True

    def setUp(self):
        # create component
        self.em = EntityMgr()
        self.component = Guard(self.em)

        # add cmd handler to it
        self.component.add_cmd_handler(Cmd.del_user, DelUser.do)

        user = User(name=Name(val="admin user"),
                    email=Email(val="admin@gnu.org"),
                    roles=[Role.admin])

        d_user = User(name=Name(val="user user"),
                    email=Email(val="user@gnu.org"),
                    roles=[Role.user])


        d_key = "kdshfkjdahfjdhfkjd"
        session = Session(user=user, role=Role.admin, key=d_key)

        self.component.em.add_user(user)
        self.component.em.add_user(d_user)
        self.component.em.add_session(session)

        self.session = session
        self.d_user = d_user
        self.user = user
        

    def tearDown(self):
        self.component = None
