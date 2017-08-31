
import traceback

from runtime.datatypes.cmd.cmd import Cmd
from runtime.objects.user.user import User

class GetRoleSet:

    @staticmethod 
    def do(obj, instr):
        print "get_role_set_in_system: %s" % instr
        userlist = obj.em.get_all(User)
        role_set = []
        for i in range(len(userlist)):
            role_list = userlist[i].get("roles")
            for j in range(len(role_list)):
                role_element = role_list[j]
                if role_element not in role_set:
                    role_set.append(role_element)
        return {'instr': instr, 'result': role_set}
