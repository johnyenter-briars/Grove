class Task(object):

    def __init__(self, taskTuple):
        super().__init__()
        self._TaskID = taskTuple[0]
        self._BranchID = taskTuple[1]
        self._StudentID = taskTuple[2]
        self._ProjectID = taskTuple[3]
        self._TaskDescription = taskTuple[4]
        self._Resolved = taskTuple[5]

    def getTaskID(self):
        return self._TaskID
    
    def getBranchID(self):
        return self._BranchID

    def getStudentId(self):
        return self._StudentID

    def getProjectID(self):
        return self._ProjectID

    def getTaskDesc(self):
        return self._TaskDescription
    
    def getResolved(self):
        return self._Resolved == 1