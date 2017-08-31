
import traceback
from  runtime.exceptions.app.exception import AppException
from runtime.utils.type_utils.type_utils import check_pred
from runtime.datatypes.cmd.cmd import Cmd
from runtime.objects.session.session import Session
from runtime.datatypes.instr.show_users.show_users_instr import ShowUsersInstr

class ShowUsers:

    @staticmethod 
    def do(component, instr):
        print "show_users: %s" % instr

        ShowUsers.check_type(instr)
        ShowUsers.check_auth(component, instr)
        ShowUsers.check_state(component, instr)
        return instr

    @staticmethod
    def check_type(instr):
        check_pred(ShowUsersInstr.is_inst)(instr)
        return instr

    @staticmethod
    def check_auth(component, instr):
        return instr

    @staticmethod
    def check_state(component, instr):
        if not component.em.is_present(instr['session']):
            raise AppException(op="show_users.chec_state",
                                   msg="session is not in the entity manager")

        return instr
