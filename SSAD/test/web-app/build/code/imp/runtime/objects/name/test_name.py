
import unittest
from unittest import TestCase
from runtime.objects.name.name import Name

class TestName(TestCase):
    TESTING = True

    def test_instantiate_name(self):
        print "test_instantiate_name"
        self.assertEqual(Name.is_inst(Name(val="Jimi Hendrix")), True)
        self.assertEqual(Name(val="Jimi Hendrix").get("val"), "Jimi Hendrix")
        self.assertRaises(TypeError, Name, val="Jimi 123 Hendrix")

    def test_name_equality(self):

        print "test_name_equality"
        self.assertEqual(Name(val="Jimi Hendrix") == 
                         Name(val="Jimi Hendrix"), 
                         True)

        self.assertEqual(Name(val="Jimi Hendrix") == 
                         Name(val="Bo Didley"), 
                         False)
