
import unittest
from unittest import TestCase
from runtime.objects.user.user import User
from runtime.objects.role.role import Role
from runtime.objects.name.name import Name
from runtime.objects.email.email import Email
from runtime.objects.session.session import Session

class TestHarness(TestCase):
    TESTING = True

    def setUp(self):
        self.user_with_no_role = User(name=Name(val="Jimi Hendrix"),
                    email=Email(val="jimi@gnu.org"),
                    roles=[])

        self.user_with_admin_role = User(name=Name(val="Jimi Admin"),
                    email=Email(val="admin@g.org"),
                    roles=[Role.admin])

        self.user_with_user_role = User(name=Name(val="Jimi User"),
                    email=Email(val="user@g.org"),
                    roles=[Role.user])

        self.user_with_both_roles = User(name=Name(val="Jimi Both"),
                    email=Email(val="both@g.org"),
                    roles=[Role.user, Role.admin])

        self.key = "123"

    def tearDown(self):
        self.user_with_no_role = None

        self.user_with_admin_role = None

        self.user_with_user_role = None

        self.user_with_both_roles = None

        self.key = None
