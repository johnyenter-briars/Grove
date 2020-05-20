class Project(object):

    def __init__(self, projectTuple):
        super().__init__()
        self._ProjectID = projectTuple[0]
        self._TeacherID = projectTuple[1]
        self._GrowthStatus = projectTuple[2]
        self._ProjectName = projectTuple[3]
        self._ProjectDescription = projectTuple[4]

    def getProjectID(self):
        return self._ProjectID

    def getTeacherID(self):
        return self._TeacherID

    def getGrowthStatus(self):
        return self._GrowthStatus

    def getProjectName(self):
        return self._ProjectName

    def getProjectDesc(self):
        return self._ProjectDescription
