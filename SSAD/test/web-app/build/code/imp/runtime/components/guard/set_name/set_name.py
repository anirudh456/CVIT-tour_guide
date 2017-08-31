
import traceback
from runtime.exceptions.app.exception import AppException
from runtime.utils.type_utils.type_utils import check_pred
from runtime.datatypes.cmd.cmd import Cmd
from runtime.objects.session.session import Session
from runtime.objects.role.role import Role
from runtime.objects.name.name import Name
from runtime.datatypes.instr.set_name.set_name_instr import SetNameInstr

class SetName:

    @staticmethod 
    def do(component, instr):
        print "set_name: %s" % instr

        SetName.check_type(instr)
        SetName.check_auth(component, instr)
        SetName.check_state(component, instr)
        return instr

    @staticmethod
    def check_type(instr):
         check_pred(SetNameInstr.is_inst)(instr)

    @staticmethod
    def check_auth(component, instr):
        session = instr['session']
        user = session.get('user')
        role = session.get('role')
        if role != Role.admin:
            if user == instr['data']['user']:
                return instr
            else: 
                raise AppException(op="set_name.check_auth",
                    msg="You cannot set the name to this user.")
        else:
            return instr
        

    @staticmethod
    def check_state(component, instr):
        if not component.em.is_present(instr['session']):
            raise AppException(op="set_name.check_state",
                                   msg="session is not in the entity manager")
        else:
            return instr
