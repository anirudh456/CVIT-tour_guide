
from runtime.datatypes.cmd.cmd import Cmd
from runtime.objects.user.user import User
from runtime.objects.role.role import Role
from runtime.objects.session.session import Session
from runtime.utils.type_utils.type_utils import dict_of
from runtime.utils.type_utils.type_utils import is_equal_to

class DelRoleInstr():

    spec = {'cmd':is_equal_to(Cmd.del_role), 
            'session': Session.is_inst,
            'data': dict_of({'user' : User.is_inst,
                             'delrole': Role.is_inst})

}

    def __init__(self):
        raise Exception("can not be instantiated!")

    @staticmethod
    def is_inst(obj):
        return dict_of(DelRoleInstr.spec)(obj)
