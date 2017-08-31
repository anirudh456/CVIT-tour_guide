
import traceback

from runtime.datatypes.cmd.cmd import Cmd
from runtime.objects.session.session import Session

class ShowSessions:

    @staticmethod 
    def do(obj, instr):
        print "show_sessions: %s" % instr
        sessions = obj.em.get_all(Session)
        return {'instr': instr, 'result': sessions}
