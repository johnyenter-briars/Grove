-- --DDL Code to Grove database

-- --1: Generate Apple Type
-- create table AppleType(
--     apple_type varchar(20) PRIMARY KEY
-- );

-- insert into AppleType values("Golden");
-- insert into AppleType values("Silver");
-- insert into AppleType values("Red");
-- insert into AppleType values("Rotten");

-- --2: Generate Role Type
-- create table RoleType(
--     permission_level varchar(20) PRIMARY KEY
-- );

-- insert into RoleType values("perm0");
-- insert into RoleType values("perm1");
-- insert into RoleType values("perm2");
-- insert into RoleType values("perm3");

-- --3: Generate Teacher table
-- create table Teacher(
--     TeacherID INTEGER,
--     FirstName varchar(20) not null,
--     LastName varchar(20) not null,
--     PermissionLevel varchar(20),
--     PRIMARY key (TeacherID),
--     FOREIGN KEY (PermissionLevel) REFERENCES RoleType(permission_level)
-- );

-- insert into Teacher (FirstName, LastName, PermissionLevel) values("Bucky", "Barnes", "perm0");
-- insert into Teacher (FirstName, LastName, PermissionLevel) values("Gamora", "Titan", "perm1");
-- insert into Teacher (FirstName, LastName, PermissionLevel) values("Peter", "Quill", "perm2");

-- -- 4: Generate Project Status
-- create table ProjectStatus(
--     GrowthStatus varchar(20) PRIMARY KEY
-- );

-- insert into ProjectStatus values("growth0");
-- insert into ProjectStatus values("growth1");
-- insert into ProjectStatus values("growth2");
-- insert into ProjectStatus values("growth3");
-- insert into ProjectStatus values("growth4");

-- 5 Generate Project Table
-- create table Project(
--     ProjectID INTEGER,
--     TeacherID INTEGER,
--     GrowthStatus varchar(20),
--     ProjectName varchar(255),
--     ProjectDescription varchar(255),
--     PRIMARY KEY (ProjectID),
--     FOREIGN KEY (TeacherID) REFERENCES Teacher(TeacherID),
--     FOREIGN KEY (GrowthStatus) REFERENCES ProjectStatus(GrowthStatus)
-- );

-- insert into Project (TeacherID, GrowthStatus, ProjectName, ProjectDescription) values(1, "growth0", "test", "test desc");

-- insert into Project (TeacherID, GrowthStatus, ProjectName, ProjectDescription) values(2, "growth3", "test", "test desc");

-- -- 6: Generate Student table
-- create table Student(
--     StudentID INTEGER,
--     FirstName varchar(20),
--     LastName varchar(20),
--     TeacherID INTEGER,
--     ProjectID INTEGER,
--     RoleType varchar(20),

--     PRIMARY KEY (StudentID),
--     FOREIGN KEY (TeacherID) REFERENCES Teacher(TeacherID),
--     FOREIGN KEY (ProjectID) REFERENCES Project(ProjectID),
--     FOREIGN KEY (RoleType) REFERENCES RoleType(permission_level)
-- );

-- insert into Student 
-- (FirstName, LastName, TeacherID, ProjectID, RoleType) 
-- values("Bruce", "Banner", 1, 1, "perm0");

-- insert into Student 
-- (FirstName, LastName, TeacherID, ProjectID, RoleType) 
-- values("Clint", "Barton", 2, 2, "perm0");

-- insert into Student 
-- (FirstName, LastName, TeacherID, ProjectID, RoleType) 
-- values("Steven", "Strange", 2, 2, "perm1");

-- insert into Student 
-- (FirstName, LastName, TeacherID, ProjectID, RoleType) 
-- values("Tony", "Stark", 3, null, "perm1");

-- insert into Student 
-- (FirstName, LastName, TeacherID, ProjectID, RoleType) 
-- values("Sam", "Wilson", 1, 1, "perm1");

-- 7: Generate Awards table
-- create table Award(
--     AwardID INTEGER,
--     StudentID INTEGER,
--     apple_type varchar(20),
--     DateAwarded TEXT,

--     PRIMARY KEY (AwardID),
--     FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
--     FOREIGN KEY (apple_type) REFERENCES AppleType(apple_type)
-- );

-- insert into Award 
-- (StudentID, apple_type, DateAwarded) 
-- values(3, "Silver", "YYYY-MM-DD HH:MM:SS.SSS");

-- insert into Award 
-- (StudentID, apple_type, DateAwarded) 
-- values(2, "Red", "YYYY-MM-DD HH:MM:SS.SSS");

-- insert into Award 
-- (StudentID, apple_type, DateAwarded) 
-- values(3, "Rotten", "YYYY-MM-DD HH:MM:SS.SSS");

-- 8 Generate Branches
-- create table Branch(
--     BranchID INTEGER,
--     StudentID INTEGER,
--     ProjectID INTEGER,
--     BranchDescription TEXT, 
--     Resolved INTEGER,
--     Weight INTEGER, 
    
--     Primary KEY (BranchID, StudentID),
--     FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
--     FOREIGN KEY (ProjectID) REFERENCES Project(ProjectID)
-- );

-- insert into Branch 
-- (BranchID, StudentID, ProjectID, BranchDescription, Resolved, Weight) 
-- values(1, 3, 2, "Add colors", 0, 100);

-- insert into Branch 
-- (BranchID, StudentID, ProjectID, BranchDescription, Resolved, Weight) 
-- values(2, 1, 1, "Update ppt", 1, 25);

-- insert into Branch 
-- (BranchID, StudentID, ProjectID, BranchDescription, Resolved, Weight) 
-- values(3, 2, 2, "Reformat document", 1, 25);

-- insert into Branch 
-- (BranchID, StudentID, ProjectID, BranchDescription, Resolved, Weight) 
-- values(3, 3, 2, "Reformat document", 1, 25);


-- 9: Generate Task table
-- create table Task(
--     TaskID INTEGER,
--     BranchID INTEGER,
--     StudentID INTEGER, 
--     ProjectID INTEGER,
--     TaskDescription TEXT,
--     Resolved INTEGER,

--     PRIMARY KEY (TaskId),
--     FOREIGN KEY (BranchID) REFERENCES Branch(BranchID),
--     FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
--     FOREIGN KEY (ProjectID) REFERENCES Project(ProjectID)
-- );

-- insert into Task
-- (BranchID, StudentID, ProjectID, TaskDescription, Resolved)
-- values(2, 1, 1, "Open power point", 0);

-- insert into Task
-- (BranchID, StudentID, ProjectID, TaskDescription, Resolved)
-- values(3, 2, 2, "Open ms word", 1);

-- insert into Task
-- (BranchID, StudentID, ProjectID, TaskDescription, Resolved)
-- values(3, 3, 2, "Click reformat button", 0);

-- 10: Chat
-- create table Chat(
--     ChatID INTEGER,
--     StudentID INTEGER,
--     TaskID INTEGER,
--     TimeStamp TEXT,
--     MessageString TEXT,

--     PRIMARY KEY (ChatID),
--     FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
--     FOREIGN KEY (TaskID) REFERENCES Task(TaskID)
-- );

-- insert into Chat
-- (StudentID, TaskID, TimeStamp, MessageString)
-- values(2, 3, "now", "All done with task number 2! You can format document now. ");

-- insert into Chat
-- (StudentID, TaskID, TimeStamp, MessageString)
-- values(3, 1, "now", "Hurry up you bum!");

-- 11: Make Admin
create table Admin(
    AdminID INTEGER,
    Name varchar(20),
    RoleType varchar(20),

    PRIMARY KEY (AdminID),
    FOREIGN KEY (RoleType) REFERENCES RoleType(permission_level)
);

insert into Admin(Name, RoleType) values("The Watcher", "perm3");

