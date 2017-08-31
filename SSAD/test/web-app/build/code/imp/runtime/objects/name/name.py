
from runtime.utils.type_utils.type_utils import is_alphabetic_str
from runtime.utils.factories.property_class_factory import PropertyClassFactory

Name = PropertyClassFactory.mk_class("Name", ['val'], val=is_alphabetic_str)
