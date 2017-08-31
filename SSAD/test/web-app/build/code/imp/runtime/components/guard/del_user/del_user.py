
import traceback
from runtime.exceptions.app.exception import AppException
from runtime.utils.type_utils.type_utils import check_pred
from runtime.datatypes.cmd.cmd import Cmd
from runtime.objects.session.session import Session
from runtime.objects.role.role import Role
from runtime.datatypes.instr.del_user.del_user_instr import DelUserInstr

class DelUser:

    @staticmethod 
    def do(obj, instr):
        print "del_user: %s" % instr

        DelUser.check_type(instr)
        DelUser.check_auth(obj, instr)
        DelUser.check_state(obj, instr)
        return instr

    @staticmethod
    def check_type(instr):
        check_pred(DelUserInstr.is_inst)(instr)

    @staticmethod
    def check_auth(obj, instr):
        session = instr['session']
        user = session.get("user")
        role = session.get("role")
        if role != Role.admin:
            raise AppException(op="del_user.check_auth", 
                msg="Only admin can delete a user")
        if user == instr['data']['user']:
            raise AppException(op="del_user.check_auth",
                msg="You cannot delete yourself")
        

    @staticmethod
    def check_state(obj, instr):
        if not obj.em.is_present(instr['session']):
            raise AppException(op="del_user.check_state", 
                msg= "session is not in the entity manager")
