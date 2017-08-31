
import traceback

from runtime.datatypes.cmd.cmd import Cmd
from runtime.objects.user.user import User

class GetRoles:

    @staticmethod 
    def do(obj, instr):
        print "get_roles_of_user: %s" % instr
        userlist = obj.em.get_all(User)
        for i in range(len(userlist)):
            if userlist[i]== instr['data']['user']:
                roles=userlist[i].get('roles')
                return {'instr': instr, 'result': roles}
