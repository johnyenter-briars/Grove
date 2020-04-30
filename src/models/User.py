class User(object):

    def __init__(self):
        super().__init__()
        self._UserID = None
        self._RoleType = None
        
    def getUserID(self):
        return self._UserID

    def setUserID(self, ID):
        self._UserID = ID

    def getRoleType(self):
        return self._RoleType

    def setRoleType(self, RoleType):
        self._RoleType = RoleType