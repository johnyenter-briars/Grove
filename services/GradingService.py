class GradingService(object):

    def __init__(self):
        super().__init__()

    def getProjectWeight(self, projectID):
        return 8

    def getProjectGoal(self, projectID):
        return 10

    def getProjectGrowthStatus(self, projectID):
        return self.getProjectWeight(projectID) / self.getProjectGoal(projectID)