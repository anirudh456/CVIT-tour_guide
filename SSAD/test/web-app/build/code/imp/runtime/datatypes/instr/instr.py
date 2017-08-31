
class Instr():

    def __init__(self):
        raise Exception("can not instantiate!")

    @staticmethod
    def is_inst(thing):
        return ShowUsersInstr.is_inst(thing) # or \
#               AddUserInstr.is_inst(thing)  # etc.

#         overkill  
#         return ormap(lambda route: route.is_inst(thing), [ShowUsersInstr])
