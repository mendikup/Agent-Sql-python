class Agent:

    def __init__(self, codeName, realName, location, status, missionsCompleated, id=None):
        self.id = id
        self.codeName = codeName
        self.realName = realName
        self.location = location
        self.status = status
        self.missionsCompleated = missionsCompleated

    def __str__(self):
        return f"agent details - id: {self.id} ||| code name: {self.codeName} ||| real name: {self.realName} ||| location: {self.location} ||| status: {self.status} ||| missions completed: {self.missionsCompleated}"
