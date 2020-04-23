class Files(object):
    def __init__(self, filesTuple):
        super().__init__()
        self._FileID = filesTuple[0]
        self._FileName = filesTuple[1]
        self._FileType = filesTuple[2]

    def getFileID(self):
        return self._FileID

    def getFileName(self):
        return self._FileName

    def getPhoto(self):
        return self._FileType
