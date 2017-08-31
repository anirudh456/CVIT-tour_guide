
import traceback
from  runtime.exceptions.app.exception import AppException
from runtime.utils.type_utils.type_utils import check_pred
from runtime.datatypes.cmd.cmd import Cmd
from runtime.objects.session.session import Session
from runtime.datatypes.instr.get_role_set_in_system.get_role_set_in_system_instr import GetRoleSetInstr

class GetRoleSet:

    @staticmethod 
    def do(component, instr):
        print "get_role_set_in_system: %s" % instr

        GetRoleSet.check_type(instr)
        GetRoleSet.check_auth(component, instr)
        GetRoleSet.check_state(component, instr)
        return instr

    @staticmethod
    def check_type(instr):
        check_pred(GetRoleSetInstr.is_inst)(instr)
        return instr

    @staticmethod
    def check_auth(component, instr):
        return instr

    @staticmethod
    def check_state(component, instr):
        if not component.em.is_present(instr['session']):
            raise AppException(op="get_role_set_in_system.chec_state",
                                   msg="session is not in the entity manager")

        return instr
