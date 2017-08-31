
from runtime.utils.type_utils.type_utils  import is_email_str
from runtime.utils.factories.property_class_factory import PropertyClassFactory

Email = PropertyClassFactory.mk_class("Email", ['val'], val=is_email_str)
