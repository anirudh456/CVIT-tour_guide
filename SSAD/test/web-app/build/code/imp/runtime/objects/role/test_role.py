
import unittest
from unittest import TestCase
from runtime.objects.role.role import Role

class TestRole(TestCase):
    TESTING = True
    def test_instantiate_role(self):
        print "test_instantiate_role"
        a_role = Role(val="admin")
        self.assertEqual(Role.is_inst(a_role), True)
        self.assertEqual(a_role.get("val"), "admin")
        self.assertRaises(TypeError, Role, my_name="admin123")

    def test_set_and_get_role(self):
        print "test_sets_on_role"
        u_role = Role(val="user")
        self.assertEqual(u_role.get("val"), "user")
        u_role.set(val="admin")
        self.assertEqual(u_role.get("val"), "admin")
