
from runtime.utils.components.generic_component import GenericComponent
class Guard(GenericComponent):

    def __init__(self, em):
        GenericComponent.__init__(self) 
        self.em = em
