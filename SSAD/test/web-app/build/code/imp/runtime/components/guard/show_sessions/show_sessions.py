
import traceback
from  runtime.exceptions.app.exception import AppException
from runtime.utils.type_utils.type_utils import check_pred
from runtime.objects.role.role import Role
from runtime.datatypes.cmd.cmd import Cmd
from runtime.objects.session.session import Session
from runtime.datatypes.instr.show_sessions.show_sessions_instr import ShowSessionsInstr

class ShowSessions:

    @staticmethod 
    def do(component, instr):
        print "show_sessions: %s" % instr

        ShowSessions.check_type(instr)
        ShowSessions.check_auth(component, instr)
        ShowSessions.check_state(component, instr)
        return instr

    @staticmethod
    def check_type(instr):
        check_pred(ShowSessionsInstr.is_inst)(instr)
        return instr

    @staticmethod
    def check_auth(component, instr):
        session = instr['session']
        user = session.get('user')
        role = session.get('role')
        if role != Role.admin:
            raise AppException(op="add_user.check_auth",
                msg="Only admin can view all sessions")
        return instr

    @staticmethod
    def check_state(component, instr):
        if not component.em.is_present(instr['session']):
            raise AppException(op="show_sessions.check_state",
                                   msg="session is not in the entity manager")

        return instr
