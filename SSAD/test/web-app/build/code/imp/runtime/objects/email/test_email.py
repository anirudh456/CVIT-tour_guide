
import unittest
from unittest import TestCase
from runtime.objects.email.email import Email

class TestEmail(TestCase):
    TESTING = True

    def test_instantiate_email(self):
        print "test_instantiate_email"
        self.assertEqual(Email.is_inst(Email(val="jhx@g.com")), True)
        self.assertEqual(Email(val="jhx@g.com").get("val"), "jhx@g.com")
        self.assertRaises(TypeError, Email, val="Jimi 123 Hendrix")

    def test_email_equality(self):

        print "test_email_equality"
        self.assertEqual(Email(val="jhx@g.com") == 
                         Email(val="jhx@g.com"), 
                         True)

        self.assertEqual(Email(val="jhx@g.com") == 
                         Email(val="bod@g.com"), 
                         False)
