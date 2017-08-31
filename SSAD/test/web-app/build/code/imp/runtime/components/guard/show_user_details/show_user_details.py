
import traceback
from  runtime.exceptions.app.exception import AppException
from runtime.utils.type_utils.type_utils import check_pred
from runtime.objects.role.role import Role
from runtime.objects.user.user import User
from runtime.datatypes.cmd.cmd import Cmd
from runtime.objects.session.session import Session
from runtime.datatypes.instr.show_user_details.show_user_details_instr import ShowDetailsInstr

class ShowDetails:

    @staticmethod 
    def do(component, instr):
        print "show_user_details: %s" % instr

        ShowDetails.check_type(instr)
        ShowDetails.check_auth(component, instr)
        ShowDetails.check_state(component, instr)
        return instr

    @staticmethod
    def check_type(instr):
        check_pred(ShowDetailsInstr.is_inst)(instr)
        return instr

    @staticmethod
    def check_auth(obj, instr):
        session = instr['session']
        userlist = obj.em.get_all(User)
        email = instr['data']['email']
        email = email.get('val')
        emails = []
        for i in range(len(userlist)):
            emails.append(userlist[i].get("email").get("val"))
        role = session.get('role')
        if role != Role.admin:
            if email in emails:
                return instr
            else: 
                raise AppException(op="show_user_details.check_auth",
                    msg="No user found")
        else:
            return instr
        

    @staticmethod
    def check_state(component, instr):
        if not component.em.is_present(instr['session']):
            raise AppException(op="show_user_details.check_state",
                                   msg="session is not in the entity manager")

        return instr
