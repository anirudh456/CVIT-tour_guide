
from runtime.utils.factories.property_class_factory import PropertyClassFactory
def is_role_str(a):
   return a == "user" or a == "admin"

Role = PropertyClassFactory.mk_class("Role", ['val'], val=is_role_str)

Role.admin = Role(val="admin")
Role.user = Role(val="user")
Role.is_admin = lambda self: self.val == "admin"
Role.is_user = lambda self: self.val == "user"
