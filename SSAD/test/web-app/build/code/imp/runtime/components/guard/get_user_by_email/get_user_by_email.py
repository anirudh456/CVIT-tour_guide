
import traceback
from runtime.exceptions.app.exception import AppException
from runtime.utils.type_utils.type_utils import check_pred
from runtime.datatypes.cmd.cmd import Cmd
from runtime.objects.user.user import User
from runtime.objects.session.session import Session
from runtime.objects.role.role import Role
from runtime.datatypes.instr.get_user_by_email.get_user_by_email_instr import GetUserInstr

class GetUser:

    @staticmethod 
    def do(component, instr):
        print "get_user_by_email: %s" % instr

        GetUser.check_type(instr)
        GetUser.check_auth(component, instr)
        GetUser.check_state(component, instr)
        return instr

    @staticmethod
    def check_type(instr):
         check_pred(GetUserInstr.is_inst)(instr)

    @staticmethod
    def check_auth(obj, instr):
        email = instr['data']['email']
        email = email.get('val')
        userlist = obj.em.get_all(User)
        emails = []
        for i in range(len(userlist)):
            emails.append(userlist[i].get("email").get("val"))
        if email not in emails:
            raise AppException(op="get_user_by_email.check_auth",
                msg="No user found")
        return instr

    @staticmethod
    def check_state(component, instr):
        if not component.em.is_present(instr['session']):
            raise AppException(op="get_user_by_emailn.check_state",
                                   msg="session is not in the entity manager")
        else:
            return instr
