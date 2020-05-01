class Teacher(object):
    def __init__(self, teacherTuple):
        super().__init__()
        self._TeacherID = teacherTuple[0]
        self._FirstName = teacherTuple[1]
        self._LastName = teacherTuple[2]
        self._PermissionLevel = teacherTuple[3]

    def getTeacherID(self):
        return self._TeacherID

    def getFirstName(self):
        return self._FirstName

    def getLastName(self):
        return self._LastName

    def getPermissionLevel(self):
        return self._PermissionLevel