
from runtime.datatypes.cmd.cmd import Cmd
from runtime.objects.session.session import Session
from runtime.utils.type_utils.type_utils import dict_of
from runtime.utils.type_utils.type_utils import is_equal_to

class ShowUsersInstr():

    spec = {'cmd':is_equal_to(Cmd.show_users), 
                   'session': Session.is_inst}

    def __init__(self):
       raise Exception("can not be instantiated!")

    @staticmethod
    def is_inst(obj):
        return dict_of(ShowUsersInstr.spec)(obj)
