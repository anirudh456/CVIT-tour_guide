
import traceback

from runtime.datatypes.cmd.cmd import Cmd
from runtime.objects.user.user import User
from runtime.objects.role.role import Role

class AddRole:

    @staticmethod 
    def do(obj, instr):
        user = instr['data']['user']
        obj.em.delete_user(user)
        addrole = instr['data']['addrole']
        user.append_role(addrole)
        rolelist = user.get('roles')
        obj.em.add_user(user)
        return {'instr': instr, 'result': rolelist}
