from models.Branch import Branch
import collections
class BranchFlattener(object):

    def __init__(self, rowTuples):
        self._rawRows = rowTuples

    def flatten(self):
        listOfBranchIds = [t[0] for t in self._rawRows]
        duplicateBranchIds = [id for id, count in collections.Counter(listOfBranchIds).items() if count > 1]
        
        #Note: this code assumes that the data in the database is correct, and that branches
        #   That share the same BranchID also share every other piece of data (except StudentId)
        
        #Generate the initial list of branch objects without the duplicates
        # tupleBranchList = [tuple in self._rawRows if tuple[0] not in duplicateIds]
        branchList = []
        for tuple in self._rawRows:
            if tuple[0] in duplicateBranchIds:
                continue
            #Have to reorganize tuple for the students on said branch to be a list
            tupleCopy = (tuple[0], [tuple[1]], tuple[2], tuple[3], tuple[4],tuple[5])
            branchList.append(Branch(tupleCopy))

        #Add back in the branch that should have both students
        for id in duplicateBranchIds:
            duplicateBranchTuples = [tuple for tuple in self._rawRows if tuple[0] == id]
            studentsOnSameBranch = [tuple[1] for tuple in duplicateBranchTuples]
            
            #Yea sorry about this, but MVP right....?
            tupleCopy = (duplicateBranchTuples[0][0], 
                        studentsOnSameBranch, 
                        duplicateBranchTuples[0][2], 
                        duplicateBranchTuples[0][3], 
                        duplicateBranchTuples[0][4],
                        duplicateBranchTuples[0][5])

            branchList.append(Branch(tupleCopy))

        return branchList

