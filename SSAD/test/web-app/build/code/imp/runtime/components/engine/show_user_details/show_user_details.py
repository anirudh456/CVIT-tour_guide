
import traceback

from runtime.datatypes.cmd.cmd import Cmd
from runtime.objects.user.user import User

class ShowDetails:

    @staticmethod 
    def do(obj, instr):
        print "show_user_details: %s" % instr
        userlist = obj.em.get_all(User)
        email = instr['data']['email']
        email = email.get("val")
        for i in range(len(userlist)):
            check = userlist[i].get("email").get("val")
            if check == email:
                user = userlist[i]
                roles_of_user = user.get('roles')
                name_of_user = user.get('name').get('val')
                email_of_user = check
                return {'instr': instr, 'result': {'roles_of_user':roles_of_user,
                                                   'name_of_user':name_of_user,
                                                   'email_of_user':email_of_user}}
