
class Cmd():

    def __init__(self, cmd_name):
        self.name = cmd_name

    def __repr__(self):
        return self.name
    
    def __hash__(self):
        return hash(self.name)

    @staticmethod
    def is_cmd(cmd):
        return cmd in Cmd.cmds

    def __eq__(self, other):
        return isinstance(other, Cmd) and self.name == other.name


Cmd.show_users = Cmd('show_users')
Cmd.add_user = Cmd('add_user')
Cmd.del_user = Cmd('del_user')
Cmd.add_role = Cmd('add_role')
Cmd.del_role = Cmd('del_role')
Cmd.show_sessions = Cmd('show_sessions')
Cmd.set_name = Cmd('set_name')
Cmd.set_email = Cmd('set_email')
Cmd.get_user_by_email = Cmd('user_by_email')
Cmd.show_user_details = Cmd('show_user_details')
Cmd.get_roles_of_user = Cmd('get_roles_of_user')
Cmd.get_role_set_in_system = Cmd('get_role_set_in_system')

Cmd.cmds = [Cmd.show_users, 
            Cmd.add_user, 
            Cmd.del_user, 
            Cmd.add_role,
            Cmd.del_role,
            Cmd.show_sessions,
            Cmd.set_name,
            Cmd.set_email,
            Cmd.get_user_by_email,
            Cmd.show_user_details,
            Cmd.get_roles_of_user,
            Cmd.get_role_set_in_system]
