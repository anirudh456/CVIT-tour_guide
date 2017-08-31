
from runtime.components.guard.guard import Guard
from runtime.components.engine.engine import Guard
from runtime.emgrs.svem.svem import EntityMgr
from runtime.components import guard
from runtime.components import engine

class GuardSysWf():
  
  def __init__(self):
     em      = EntityMgr()
     guard   = Guard(em)
     engine  = Engine(em)

     # set up routes in the guard
     guard.add_command_handler(Cmd.add_user, guard.add_user.add_user.AddUser.do)
     guard.add_command_handler(Cmd.del_user, guard.del_user.del_user.DelUser.do)
     guard.add_command_handler(Cmd.show_users, guard.show_users.show_users.ShowUsers.do)
     guard.add_command_handler(Cmd.show_sessions, guard.show_sessions.show_sessions.ShowSessions.do)
     guard.add_command_handler(Cmd.add_role, guard.add_role.add_role.AddRole.do)
     guard.add_command_handler(Cmd.del_role, guard.del_role.del_role.DelRole.do)
     guard.add_command_handler(Cmd.set_email, guard.set_email.set_email.SetEmail.do)
     guard.add_command_handler(Cmd.set_name, guard.set_name.set_name.SetName.do)


     # set up routes in the engine
     engine.add_command_handler(Cmd.add_user, engine.add_user.add_user.AddUser.do)
     engine.add_command_handler(Cmd.del_user, engine.del_user.del_user.DelUser.do)
     engine.add_command_handler(Cmd.show_users, engine.show_users.show_users.ShowUsers.do)
     engine.add_command_handler(Cmd.add_role, engine.add_role.add_role.AddRole.do)
     engine.add_command_handler(Cmd.del_role, engine.del_role.del_role.DelRole.do)
     engine.add_command_handler(Cmd.show_sessions, engine.show_sessions.show_sessions.ShowSessions.do)
     engine.add_command_handler(Cmd.set_email, engine.set_email.set_email.SetEmail.do)
     engine.add_command_handler(Cmd.set_name, engine.set_name.set_name.SetName.do)


     self.em = em
     self.guard = guard
     self.engine = engine

  def run(instr):
    result = None
    try:
      # action same as instr
      action = self.guard.do(instr)
      result = self.sys.do(action)
    except Exception as e:
      result = e
    finally:
      return result
