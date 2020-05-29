from services.DatabaseService import DatabaseService

MAX_APPLES = 5

class GradingService(object):

    def __init__(self, databaseService: DatabaseService):
        super().__init__()
        self._databaseService = databaseService

    def getCompletedProjectWeight(self, projectID):
        tasks = self._databaseService.getTasksForProject(projectID)
        taskReviews = self._databaseService.getTaskReviewsForProject(projectID)
        projectweight = 0
        for taskR in taskReviews:
            targetTasks = list(filter(lambda t: t.getTaskID() == taskR.getTaskID(), tasks))
            if len(targetTasks) > 1: raise Exception("Somehow duplicate tasks in database!")
            projectweight += (taskR.getRating() / MAX_APPLES) * targetTasks[0].getWeight()

        return round(projectweight, 2)

    def getProjectGoal(self, projectID):
        goalObj = self._databaseService.getGoalForProject(projectID)
        
        return goalObj.getProjectTargetWeight()

    def getProjectGrowthStatus(self, projectID):
        raw = self.getCompletedProjectWeight(projectID) / self.getProjectGoal(projectID)
        
        return round(raw, 2) * 100