
import copy
from runtime.utils.type_utils.type_utils import check
from runtime.utils.entitymgrs.volatile.unsafe.uvem import UnsafeVolatileEntityMgr
from  runtime.utils.entitymgrs.volatile.volatile_entity_mgr_exception import VolatileEntityMgrException

class SafeVolatileEntityMgr(UnsafeVolatileEntityMgr):
    def __init__(self):
       UnsafeVolatileEntityMgr.__init__(self)

    def safe_add(self, entity):
        check(lambda e: not self.is_present(e),
              VolatileEntityMgrException(op="safe_add", 
                  msg="entity %s already present" % entity.to_client()))(entity)

        self.unsafe_add(entity)

    def safe_delete(self, entity):
        check(self.is_present, 
              VolatileEntityMgrException(op="safe_delete", 
                  msg="entity %s not present" % entity.to_client()))(entity)

        self.unsafe_delete(entity)

    def safe_update(self, entity, **args):
        check(self.is_present,    # 1
              VolatileEntityMgrException(op="safe_update", 
                  msg="entity %s not present" % entity.to_client()))(entity)

        new_entity=copy.copy(entity) #2
        new_entity.set(**args)       #3
        if new_entity == entity:     #4
            self.unsafe_delete(entity)  #a
            self.unsafe_add(new_entity) #b
        else:
            self.safe_add(new_entity)   #c
            self.unsafe_delete(entity)  #d
