
from runtime.utils.type_utils.type_utils import is_str
from runtime.utils.factories.property_class_factory import PropertyClassFactory
from runtime.objects.user.user import User
from runtime.objects.role.role import Role

Session = PropertyClassFactory.mk_class("Session", ["key"], 
            user=User.is_inst, role=Role.is_inst, 
            key=is_str, inv=(lambda obj, args: \
                              args['role'] in \
                              args['user'].get('roles')))
