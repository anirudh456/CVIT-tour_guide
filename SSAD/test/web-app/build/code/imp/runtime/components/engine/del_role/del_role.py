
import traceback

from runtime.datatypes.cmd.cmd import Cmd
from runtime.objects.user.user import User

class DelRole:

    @staticmethod 
    def do(obj, instr):
        user = instr['data']['user']
        obj.em.delete_user(user)
        delrole = instr['data']['delrole']
        user.remove_role(delrole)
        rolelist = user.get('roles')
        obj.em.add_user(user)
        return {'instr': instr, 'result': rolelist}
