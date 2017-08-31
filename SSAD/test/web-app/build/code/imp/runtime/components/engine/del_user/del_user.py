
import traceback

from runtime.datatypes.cmd.cmd import Cmd
from runtime.objects.user.user import User

class DelUser:

    @staticmethod 
    def do(obj, instr):
        print "del_user: %s" % instr
        user = instr['data']['user']
        obj.em.delete_user(user)
        return {'instr': instr, 'result': True}
