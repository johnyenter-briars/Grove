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
        currentProject = self._databaseService.getProject(projectID)
        growthPercentage = round(raw, 2) * 100
        growthString = self.getGrowthString(growthPercentage)

        if growthString != currentProject.getGrowthStatus():
            self._databaseService.updateGrowthStatus(projectID, growthString)

        return round(growthPercentage, 2)

    def getGrowthString(self, percentage: int):
        if percentage < 0 and percentage < 20:
            return "growth0"
        elif percentage < 40:
            return "growth1"
        elif percentage < 60:
            return "growth2"
        elif percentage < 80:
            return "growth3"
        elif percentage <=100:
            return "growth4"
