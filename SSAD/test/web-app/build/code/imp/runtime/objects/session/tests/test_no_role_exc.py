
from runtime.objects.session.session import Session
from runtime.objects.session.tests.test_harness import TestHarness

class TestSessionWithNoRole(TestHarness):

    def test_session_with_no_role(self):
        with self.assertRaises(Exception):
            Session(user=self.user_with_no_role, key=self.key)
