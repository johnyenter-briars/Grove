class MessageNotifications(object):

    def __init__(self, messageTuple):
        super().__init__()
        self._NotificationID = messageTuple[0]
        self._MessageContent = messageTuple[1]
        self._TaskID = messageTuple[2]
        self._Viewed = messageTuple[3]
        self._StudentID = messageTuple[4]

    def getTaskID(self):
        return self._TaskID
    
    def getStudentId(self):
        return self._StudentID

    def getMessage(self):
        return self._MessageContent

    def getNotificationID(self):
        return self._NotificationID

    def getViewed(self):
        return self._Viewed == 1