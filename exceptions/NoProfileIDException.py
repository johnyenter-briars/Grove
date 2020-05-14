class NoProfileIDException(Exception):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._messageString = "The user navigated to a page without providing a profileID in the query string"