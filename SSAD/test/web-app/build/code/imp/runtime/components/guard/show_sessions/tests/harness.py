
import unittest
from unittest import TestCase
from runtime.components.guard.guard import Guard
from runtime.components.guard.show_sessions.show_sessions import ShowSessions
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
        self.component.add_cmd_handler(Cmd.show_sessions, ShowSessions.do)

        role = Role(val="admin")
        user = User(name=Name(val="Jimi Hendrix"),
                    email=Email(val="jimi@gnu.org"),
                    roles=[Role.admin,Role.user])

        d_key = "kdshfkjdahfjdhfkld"
        session = Session(user=user, role=Role.admin, key=d_key)

        self.component.em.add_user(user)
        self.component.em.add_session(session)
        self.session = session

    def tearDown(self):
        self.component = None
