
import traceback
from runtime.exceptions.app.exception import AppException
from runtime.utils.type_utils.type_utils import check_pred
from runtime.datatypes.cmd.cmd import Cmd
from runtime.objects.session.session import Session
from runtime.objects.role.role import Role
from runtime.datatypes.instr.del_role.del_role_instr import DelRoleInstr

class DelRole:

    @staticmethod 
    def do(component, instr):
        print "del_role: %s" % instr

        DelRole.check_type(instr)
        DelRole.check_auth(component, instr)
        DelRole.check_state(component, instr)
        return instr

    @staticmethod
    def check_type(instr):
         check_pred(DelRoleInstr.is_inst)(instr)

    @staticmethod
    def check_auth(obj, instr):
        session = instr['session']
        
        role = session.get("role")
        user = instr['data']['user']
        roles = user.get('roles')
        delrole = instr['data']['delrole']
        if role != Role.admin:
            raise AppException(op="del_role.check_auth", 
                msg="Only admin can delete a role")
        if not delrole in roles and len(roles) > 1 :
            raise AppException(op="del_role.check_auth",
                msg="cannot delete the role.")
        return instr
        

    @staticmethod
    def check_state(component, instr):
        if not component.em.is_present(instr['session']):
            raise AppException(op="del_role.check_state",
                                   msg="session is not in the entity manager")
        else:
            return instr
