
import unittest
from unittest import TestCase

from runtime.objects.email.email import Email
from runtime.objects.name.name import Name
from runtime.objects.role.role import Role
from runtime.objects.user.user import User


class TestUser(TestCase):
    TESTING = True

    def test_instantiate_user(self):
        print "test_instantiate_user"
        user = User(name=Name(val="Jimi Hendrix"),
                    email=Email(val="jimi@gnu.org"),
                    roles=[])

        self.assertEqual(User.is_inst(user), True)

    def test_sets_on_user(self):
        print "test_sets_on_user"
        user = User(name=Name(val="Jimi Hendrix"),
                    email=Email(val="jimi@gnu.org"),
                    roles=[Role(val="user")])

        user.set(email=Email(val="tmp@abc.com"))

        self.assertEqual(user.get("name").get("val"), "Jimi Hendrix")
        self.assertEqual(user.get("email").get("val"), "tmp@abc.com")
        self.assertEqual(user.get("roles")[0].get("val"), "user")

    def test_equality_on_user(self):
        print "test_equality_on_user"
        user1 = User(name=Name(val="Jimi Hendrix"),
                     email=Email(val="jimi@gnu.org"),
                     roles=[])

        user2 = User(name=Name(val="Jimi Hendrix"),
                     email=Email(val="jimi@gnu.org"),
                     roles=[]) 

        user3 = User(name=Name(val="John Roy"),
                     email=Email(val="roy@gnu.org"),
                     roles=[])

        self.assertEqual(user1 == user2, True)
        self.assertEqual(user1 == user3, False)
        
    def test_append_role(self):
        print "test_append_role"
        user = User(name=Name(val="Jimi Hendrix"),
                     email=Email(val="jimi@gnu.org"),
                     roles=[])

        user.append_role(Role(val="user"))
        self.assertTrue(len(user.get('roles')) == 1)

    def test_remove_role(self):
        print "test_remove_role"
        user = User(name=Name(val="Jimi Hendrix"),
                     email=Email(val="jimi@gnu.org"),
                     roles=[Role.user,Role.admin])

        user.remove_role(Role(val="user"))
        self.assertTrue(len(user.get('roles')) == 1)
