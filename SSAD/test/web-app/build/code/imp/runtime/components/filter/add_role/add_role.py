
import traceback

from runtime.datatypes.cmd.cmd import Cmd
from runtime.objects.user.user import User
from runtime.objects.role.role import Role

class AddRole:

    @staticmethod 
    def do(obj, instr):
        user = instr['data']['user']
        
        rolelist = user.get('roles')
        
        return {'instr': instr, 'result': rolelist}
