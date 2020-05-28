from _datetime import datetime

class Chat(object):
    from time import strftime
    def __init__(self, chatTuple):
        super().__init__()
        self._ChatID = chatTuple[0]
        self._UserName = chatTuple[1]
        self._TaskID = chatTuple[2]
        self._TimeStamp = chatTuple[3]
        self._MessageString = chatTuple[4]

    def getChatID(self):
        return self._ChatID

    def getUserName(self):
        return self._UserName

    def getTimeStamp(self):
        timestamp = datetime.fromtimestamp(self._TimeStamp)
        return timestamp.strftime("%x %I:%M:%S %p")
    
    def getRawTime(self):
        return self._TimeStamp

    def getMessageString(self):
        return self._MessageString

    def getTaskID(self):
        return self._TaskID
