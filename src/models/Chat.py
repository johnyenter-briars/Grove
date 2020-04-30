class Chat(object):
    def __init__(self, chatTuple):
        super().__init__()
        self._ChatID = chatTuple[0]
        self._StudentID = chatTuple[1]
        self._TaskID = chatTuple[2]
        self._TimeStamp = chatTuple[3]
        self._MessageString = chatTuple[4]

    def getChatID(self):
        return self._ChatID

    def getStudentID(self):
        return self._StudentID

    def getTimeStamp(self):
        return self._TimeStamp

    def getMessageString(self):
        return self._MessageString

    def getTaskID(self):
        return self._TaskID
