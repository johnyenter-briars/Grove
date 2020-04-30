class Award(object):

    def __init__(self, awardTuple):
        super().__init__()
        self._AwardID = awardTuple[0]
        self._StudentID = awardTuple[1]
        self._apple_type = awardTuple[2]
        self._DateAwarded = awardTuple[3]

    def getAwardID(self):
        return self._AwardID

    def getStudentID(self):
        return self._StudentID

    def getAppleType(self):
        return self._apple_type

    def getDateAwarded(self):
        return self._DateAwarded