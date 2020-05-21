class Apple(object):

    def __init__(self, appleTuple):
        super().__init__()
        self._AppleType = appleTuple[0] 

    def getAppleType(self):
        return self._AppleType