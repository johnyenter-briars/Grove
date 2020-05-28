class Student(object):
    def __init__(self, studentTuple):
        super().__init__()
        self._StudentID = studentTuple[0]
        self._FirstName = studentTuple[1]
        self._LastName = studentTuple[2]
        self._TeacherID = studentTuple[3]
        self._ProjectID = studentTuple[4]
        self._RoleType = studentTuple[5]
        self._ApplesAwarded = studentTuple[6]

    def getStudentID(self):
        return self._StudentID

    def getFirstName(self):
        return self._FirstName

    def getLastName(self):
        return self._LastName

    def getTeacherID(self):
        return self._TeacherID

    def getProjectID(self):
        return self._ProjectID

    def getRoleType(self):
        return self._RoleType

    def getApplesAwarded(self):
        return self._ApplesAwarded