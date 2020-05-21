class TaskReview(object):

    def __init__(self, taskTuple):
        super().__init__()
        self._ReviewID = taskTuple[0]
        self._TaskID = taskTuple[1]
        self._Resolved = taskTuple[2]
        self._Rating = taskTuple[3]

    def getTaskID(self):
        return self._TaskID
    
    def getReviewID(self):
        return self._ReviewID

    def getResolved(self):
        return self._Resolved == 1
    
    def getRating(self):
        return self._Rating