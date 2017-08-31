
from runtime.datatypes.cmd.cmd import Cmd
from runtime.objects.user.user import User
from runtime.objects.session.session import Session
from runtime.utils.type_utils.type_utils import dict_of
from runtime.utils.type_utils.type_utils import is_equal_to

class AddUserInstr():

    spec = {'cmd':is_equal_to(Cmd.add_user), 
            'session': Session.is_inst,
            'data': dict_of({'user' : User.is_inst})}

    def __init__(self):
        raise Exception("can not be instantiated!")

    @staticmethod
    def is_inst(obj):
        return dict_of(AddUserInstr.spec)(obj)
