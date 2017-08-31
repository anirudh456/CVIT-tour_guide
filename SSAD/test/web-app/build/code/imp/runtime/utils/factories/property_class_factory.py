
from  runtime.utils.class_templates.class_templates import ClassTemplate
from  runtime.utils.type_utils.type_utils import is_inst
from  runtime.utils.type_utils.type_utils import check_pred
class PropertyClassFactory():

#    User = mk_class("User", ['email'], email=Email.is_inst, name=Name.is_inst)
    @staticmethod
    def mk_class(_name, _unique_keys, **args):
        cls = ClassTemplate.mk_class(_name)
        cls.is_inst = staticmethod(is_inst(cls))
        cls.check_inst = staticmethod(check_pred(cls.is_inst))
        cls.add_attributes(**args)
        cls.__eq__ = lambda self, other: \
                         self.is_inst(other) and \
                         all(map(lambda key: self.get(key) == other.get(key),
                                 _unique_keys))
        return cls
