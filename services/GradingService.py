from services.DatabaseService import DatabaseService
class GradingService(object):

    def __init__(self, databaseService: DatabaseService):
        super().__init__()
        self._databaseService = databaseService

    def getCompletedProjectWeight(self, projectID):
        branches = self._databaseService.getBranchesForProject(projectID)
        
        return sum([branch.getWeight() for branch in branches if branch.getResolved()])

    def getProjectGoal(self, projectID):
        goalObj = self._databaseService.getGoalForProject(projectID)
        
        return goalObj.getProjectTargetWeight()

    def getProjectGrowthStatus(self, projectID):
        raw = self.getCompletedProjectWeight(projectID) / self.getProjectGoal(projectID)
        
        return round(raw, 2) * 100