class UserCredentials(object):
    def __init__(self, userCredentialsTuple):
        super().__init__()
        self._UserCredentialsID = userCredentialsTuple[0]
        self._UserID = userCredentialsTuple[1]
        self._UserType = userCredentialsTuple[2]
        self._UserName = userCredentialsTuple[3]
        self._UserPass = userCredentialsTuple[4]

    def getUserCredentialsID(self):
        return self._UserCredentialsID

    def getUserID(self):
        return self._UserID

    def getUserType(self):
        return self._UserType

    def getUserName(self):
        return self._UserName

    def getUserPass(self):
        return self._UserPass