
class UnsafeVolatileEntityMgr():
    def __init__(self):
        # this store is volatile
        self.db = {}

    def mk_volatile_entity(self, cls):
        cls = type(cls.__name__, (object,), dict(cls.__dict__))
        self.db[cls] = []
        return cls


    def register_as_entity(self, cls):
        self.db[cls] = []


    # tests if entity is in aggregate
    def is_present(self, entity):
        return entity in self.db[entity.__class__]



    # assumes entity is not present in aggregate
    def unsafe_add(self, entity):
        entity_set = self.db[entity.__class__]
        entity_set.append(entity)

    # assumes entity is in aggregate
    def unsafe_delete(self, entity):
        entity_set = self.db[entity.__class__]
        entity_set.remove(entity)

    # assumes entity is in aggregate
    def unsafe_update(self, entity, **args):
        pass

    # assumes cls is the entity class    
    def get_all(self, cls):
        return self.db[cls]

    # usage: apply_filters(User, email=e1, name=n1)
    def apply_filters(self, cls, **args):
        entities = self.get_all(cls)

        for key, val in  args.iteritems():
           entities = filter(lambda e: e.get(key) == val, entities)
        return entities
