
from runtime.utils.type_utils.type_utils import list_of
from runtime.utils.factories.property_class_factory import PropertyClassFactory
from runtime.objects.email.email import Email
from runtime.objects.name.name import Name
from runtime.objects.role.role import Role

User = PropertyClassFactory.mk_class("User", ['email'], 
                                     email=Email.is_inst, 
                                     name=Name.is_inst,
                                     roles=list_of(Role.is_inst))


def append_role(self, role):
    if Role.is_inst(role):
        roles = self.get('roles')
        roles.append(role)
        self.set(roles=roles)

User.append_role = append_role

def remove_role(self, role):
    if Role.is_inst(role):
        roles = self.get('roles')
        roles.remove(role)
        self.set(roles=roles)

User.remove_role = remove_role
