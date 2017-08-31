
import traceback

from runtime.datatypes.cmd.cmd import Cmd
from runtime.objects.user.user import User

class GetUser:

    @staticmethod 
    def do(obj, instr):
        print "get_user_by_email: %s" % instr
        userlist = obj.em.get_all(User)
        email = instr['data']['email']
        email = email.get("val")
        for i in range(len(userlist)):
            check = userlist[i].get("email").get("val")
            if email == check:
                user = userlist[i]
                return {'instr': instr, 'result': user}
