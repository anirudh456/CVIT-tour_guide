
from  runtime.objects.user.user import User
from  runtime.objects.session.session import Session
from  runtime.utils.entitymgrs.volatile.safe.svem import SafeVolatileEntityMgr
from runtime.utils.type_utils.type_utils import check_pred

class EntityMgr(SafeVolatileEntityMgr):
    def __init__(self):

        SafeVolatileEntityMgr.__init__(self)

        self.register_as_entity(User)
        self.register_as_entity(Session)

    def add_user(self, user):
        # check if user satisfies the User.is_inst predicate
        # i.e., if user is an instance of User
        check_pred(User.is_inst)(user)
        self.safe_add(user)

    def delete_user(self, user):
        check_pred(User.is_inst)(user)
        # make sure there is no session whose user is the given user 
        check_pred(lambda u: self.apply_filters(Session, user=u) == [])(user)
        self.safe_delete(user)

    def update_user(self, user, **args):
        check_pred(User.is_inst)(user)
        self.safe_update(user, **args)

    def add_session(self, session):
        check_pred(Session.is_inst)(session)
        # make sure that the user of the session
        # exists in the user set
        check_pred(lambda s: self.is_present(s.get('user')))(session)
        self.safe_add(session)

    def delete_session(self, session):
        check_pred(Session.is_inst)(session)
        self.safe_delete(session)

    def update_session(self, session, **args):
        check_pred(Session.is_inst)(session)
        self.safe_update(session, **args)
