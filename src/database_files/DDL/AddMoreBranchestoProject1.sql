/*
    REMEMBER:
    Because of joine Primary key of BranchID and StudentID in Branch table
    BRANCHID IS NOT AUTOINCREMENT
    You MUST specify a branch ID (either new or existing) when inserting into table
*/
insert into Branch 
(BranchId, StudentID, ProjectID, BranchDescription, Resolved, Weight) 
values (1, 1, 1, "Add pictures", 0, 10);


insert into Branch 
(BranchId, StudentID, ProjectID, BranchDescription, Resolved, Weight) 
values (3, 5, 1, "Change font in document", 0, 5);


insert into Branch 
(BranchID, StudentID, ProjectID, BranchDescription, Resolved, Weight) 
values (2, 5, 1, "Update ppt", 1, 25);

