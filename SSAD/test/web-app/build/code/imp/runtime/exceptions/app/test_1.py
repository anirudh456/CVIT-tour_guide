
import unittest
from unittest import TestCase
import traceback
# from runtime.exceptions.custom_exceptions.app.exception  import AppException
from exception  import AppException

class Test1(TestCase):
    TESTING = True

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_raise_malformed_request_exception(self):
        print "test_raise_malformed_request_exception"
        with self.assertRaises(AppException):
            raise AppException(msg="malformed request", 
                               request={'a':5},
                               session={'key':'123'},
                               tb=repr(traceback.extract_stack()))

if __name__ == '__main__':
    unittest.main()
