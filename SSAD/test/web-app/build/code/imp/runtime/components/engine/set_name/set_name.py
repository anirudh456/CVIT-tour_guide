
import traceback

from runtime.datatypes.cmd.cmd import Cmd
from runtime.objects.user.user import User
from runtime.objects.name.name import Name

class SetName:

    @staticmethod 
    def do(obj, instr):
        print "set_name: %s" % instr
        user = instr['data']['user']
        setname = instr['data']['setname']
        setname = setname.get("val")
        obj.em.delete_user(user)
        user.set( name = Name(val=setname))
        obj.em.add_user(user)
        return {'instr': instr, 'result': user}
