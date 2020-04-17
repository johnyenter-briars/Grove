from json import JSONEncoder
class ClassEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__ 