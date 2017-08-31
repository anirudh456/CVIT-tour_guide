
import traceback
from runtime.exceptions.app.exception import AppException
from runtime.utils.type_utils.type_utils import check_pred
from runtime.datatypes.cmd.cmd import Cmd
from runtime.objects.session.session import Session
from runtime.objects.role.role import Role
from runtime.objects.email.email import Email
from runtime.objects.user.user import User
from runtime.datatypes.instr.set_email.set_email_instr import SetEmailInstr

class SetEmail:

    @staticmethod 
    def do(component, instr):
        print "set_email: %s" % instr

        SetEmail.check_type(instr)
        SetEmail.check_auth(component, instr)
        SetEmail.check_state(component, instr)
        return instr

    @staticmethod
    def check_type(instr):
         check_pred(SetEmailInstr.is_inst)(instr)

    @staticmethod
    def check_auth(component, instr):
        session = instr['session']
        user = session.get('user')
        role = session.get('role')
        setemail = instr['data']['setemail']
        setemail = setemail.get('val')
        setuser = instr['data']['user']
        emails = []
        userlist = component.em.get_all(User)
        for i in range(len(userlist)):
            emails.append(userlist[i].get("email").get("val"))
        if not setemail in emails:
            if role != Role.admin:
                if setuser != user:
                    raise AppException(op="set_email.check_auth",
                        msg="You cannot set the email to this user.")
                return instr
            return instr
        raise AppException(op="set_email.check_auth",
                        msg="This email cannot be used.")

    @staticmethod
    def check_state(component, instr):
        if not component.em.is_present(instr['session']):
            raise AppException(op="set_email.check_state",
                                   msg="session is not in the entity manager")
        else:
            return instr
