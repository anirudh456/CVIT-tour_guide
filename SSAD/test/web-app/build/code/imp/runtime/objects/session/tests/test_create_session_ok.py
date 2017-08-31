
from runtime.objects.session.session import Session
from runtime.objects.role.role import Role
from runtime.objects.session.tests.test_harness import TestHarness

class TestCreateSessionOk(TestHarness):

    def test_session_user_with_admin_role(self):
        print "test_session_user_with_admin_role"

        session = Session(user=self.user_with_admin_role, key=self.key, role=Role.admin)
        self.assertEquals(session.get('user'), self.user_with_admin_role)

    def test_user_with_user_role(self):
        print "test_session_user_with_user_role"

        session = Session(user=self.user_with_user_role, key=self.key, role=Role.user)
        self.assertEquals(session.get('user'), self.user_with_user_role)
