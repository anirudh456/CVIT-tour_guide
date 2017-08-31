
import traceback
from runtime.exceptions.app.exception import AppException
from runtime.utils.type_utils.type_utils import check_pred
from runtime.datatypes.cmd.cmd import Cmd
from runtime.objects.session.session import Session
from runtime.objects.role.role import Role
from runtime.datatypes.instr.add_role.add_role_instr import AddRoleInstr

class AddRole:

    @staticmethod 
    def do(component, instr):
        print "add_role: %s" % instr

        AddRole.check_type(instr)
        AddRole.check_auth(component, instr)
        AddRole.check_state(component, instr)
        return instr

    @staticmethod
    def check_type(instr):
         check_pred(AddRoleInstr.is_inst)(instr)

    @staticmethod
    def check_auth(obj, instr):
        session = instr['session']
        
        role = session.get("role")
        user = instr['data']['user']
        roles = user.get('roles')
        addrole = instr['data']['addrole']
        if role != Role.admin:
            raise AppException(op="add_role.check_auth", 
                msg="Only admin can add a role")
        if addrole in roles :
            raise AppException(op="add_role.check_auth",
                msg="cannot add role")
        return instr
        

    @staticmethod
    def check_state(component, instr):
        if not component.em.is_present(instr['session']):
            raise AppException(op="add_role.check_state",
                                   msg="session is not in the entity manager")
        else:
            return instr
