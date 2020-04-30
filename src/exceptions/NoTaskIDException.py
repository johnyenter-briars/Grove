class NoTaskIDException(Exception):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._messageString = "The user navigated to a page without providing a taskID in the query string"

    def getMessageString():
        return self._messageString