class Goal(object):

    def __init__(self, goalTuple):
        super().__init__()
        self._GoalID = goalTuple[0]
        self._ProjectID = goalTuple[1]
        self._ProjectTargetWeight = goalTuple[2]

    def getGoalID(self):
        return self._GoalID

    def getProjectID(self):
        return self._ProjectID
    
    def getProjectTargetWeight(self):
        return self._ProjectTargetWeight
