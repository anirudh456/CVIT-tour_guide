
import traceback
from runtime.exceptions.app.exception import AppException
from runtime.utils.type_utils.type_utils import check_pred
from runtime.datatypes.cmd.cmd import Cmd
from runtime.objects.session.session import Session
from runtime.objects.role.role import Role
from runtime.datatypes.instr.add_user.add_user_instr import AddUserInstr

class AddUser:

    @staticmethod 
    def do(component, instr):
        print "add_user: %s" % instr

        AddUser.check_type(instr)
        AddUser.check_auth(component, instr)
        AddUser.check_state(component, instr)
        return instr

    @staticmethod
    def check_type(instr):
         check_pred(AddUserInstr.is_inst)(instr)

    @staticmethod
    def check_auth(component, instr):
        session = instr['session']
        user = session.get('user')
        role = session.get('role')
        if role != Role.admin:
            raise AppException(op="add_user.check_auth",
                msg="Only admin can create user")
        return instr

    @staticmethod
    def check_state(component, instr):
        if not component.em.is_present(instr['session']):
            raise AppException(op="add_user.check_state",
                                   msg="session is not in the entity manager")
        else:
            return instr
