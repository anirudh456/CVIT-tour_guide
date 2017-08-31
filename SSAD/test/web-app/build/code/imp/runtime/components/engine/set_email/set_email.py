
import traceback

from runtime.datatypes.cmd.cmd import Cmd
from runtime.objects.user.user import User
from runtime.objects.email.email import Email

class SetEmail:

    @staticmethod 
    def do(obj, instr):
        print "set_email: %s" % instr
        user = instr['data']['user']
        setemail = instr['data']['setemail']
        setemail = setemail.get("val")
        obj.em.delete_user(user)
        user.set(email = Email(val=setemail))
        obj.em.add_user(user)
        return {'instr': instr, 'result': user}
