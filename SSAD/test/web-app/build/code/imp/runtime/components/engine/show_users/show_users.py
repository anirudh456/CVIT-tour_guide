
import traceback

from runtime.datatypes.cmd.cmd import Cmd
from runtime.objects.user.user import User

class ShowUsers:

    @staticmethod 
    def do(obj, instr):
        print "show_users: %s" % instr
        users = obj.em.get_all(User)
        return {'instr': instr, 'result': users}
