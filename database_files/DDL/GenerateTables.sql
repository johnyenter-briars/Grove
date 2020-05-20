--Run this script after every merge, pull or rebase
--It will reset the database back to it's original state
drop table UserCredentials;
drop table Admin;
drop table Chat;
drop table Task;
drop table Branch;
drop table Award;
drop table Student;
drop table Project;
drop table ProjectStatus;
drop table Teacher;
drop table RoleType;
drop table AppleType;
drop table Files;
drop table ProjectGoal;

create table AppleType(
    apple_type varchar(20) PRIMARY KEY
);

insert into AppleType values("Golden");
insert into AppleType values("Silver");
insert into AppleType values("Red");
insert into AppleType values("Rotten");

create table RoleType(
    permission_level varchar(20) PRIMARY KEY
);

insert into RoleType values("perm0");
insert into RoleType values("perm1");
insert into RoleType values("perm2");
insert into RoleType values("perm3");

create table Teacher(
    TeacherID INTEGER,
    FirstName varchar(20) not null,
    LastName varchar(20) not null,
    PermissionLevel varchar(20),
    PRIMARY key (TeacherID),
    FOREIGN KEY (PermissionLevel) REFERENCES RoleType(permission_level)
);

insert into Teacher (FirstName, LastName, PermissionLevel) values("Bucky", "Barnes", "perm1");
insert into Teacher (FirstName, LastName, PermissionLevel) values("Gamora", "Titan", "perm1");
insert into Teacher (FirstName, LastName, PermissionLevel) values("Peter", "Quill", "perm1");

create table ProjectStatus(
    GrowthStatus varchar(20) PRIMARY KEY
);

insert into ProjectStatus values("growth0");
insert into ProjectStatus values("growth1");
insert into ProjectStatus values("growth2");
insert into ProjectStatus values("growth3");
insert into ProjectStatus values("growth4");

create table Project(
    ProjectID INTEGER,
    TeacherID INTEGER,
    GrowthStatus varchar(20),
    ProjectName varchar(255),
    ProjectDescription varchar(255),
    PRIMARY KEY (ProjectID),
    FOREIGN KEY (TeacherID) REFERENCES Teacher(TeacherID),
    FOREIGN KEY (GrowthStatus) REFERENCES ProjectStatus(GrowthStatus)
);

insert into Project (TeacherID, GrowthStatus, ProjectName, ProjectDescription) values(1, "growth0", "American History Presentation", "Construct presentation materials to better communicate the intricacies of American History.");

insert into Project (TeacherID, GrowthStatus, ProjectName, ProjectDescription) values(2, "growth3", "Ethics Essay", "Write our essay on Socratic ethics.");

insert into Project (TeacherID, GrowthStatus, ProjectName, ProjectDescription) values(1, "growth0", "Construct Meta-Diorama", "Make a diorama about us as a group making a diorama.");

create table Student(
    StudentID INTEGER,
    FirstName varchar(20),
    LastName varchar(20),
    TeacherID INTEGER,
    ProjectID INTEGER,
    RoleType varchar(20),

    PRIMARY KEY (StudentID),
    FOREIGN KEY (TeacherID) REFERENCES Teacher(TeacherID),
    FOREIGN KEY (ProjectID) REFERENCES Project(ProjectID),
    FOREIGN KEY (RoleType) REFERENCES RoleType(permission_level)
);

insert into Student 
(FirstName, LastName, TeacherID, ProjectID, RoleType) 
values("Thomas", "Muscarello", 1, 1, "perm2");

insert into Student 
(FirstName, LastName, TeacherID, ProjectID, RoleType) 
values("Clint", "Barton", 2, 2, "perm2");

insert into Student 
(FirstName, LastName, TeacherID, ProjectID, RoleType) 
values("Steven", "Strange", 2, 2, "perm2");

insert into Student 
(FirstName, LastName, TeacherID, ProjectID, RoleType) 
values("Tony", "Stark", 3, null, "perm2");

insert into Student 
(FirstName, LastName, TeacherID, ProjectID, RoleType) 
values("Sam", "Wilson", 1, 1, "perm2");

insert into Student 
(FirstName, LastName, TeacherID, ProjectID, RoleType) 
values("Wanda", "Maximoff", 1, 1, "perm2");

insert into Student 
(FirstName, LastName, TeacherID, ProjectID, RoleType) 
values("Pietro", "Maximoff", 1, 1, "perm2");

insert into Student 
(FirstName, LastName, TeacherID, ProjectID, RoleType) 
values("Peter", "Parker", 1, 3, "perm2");

insert into Student 
(FirstName, LastName, TeacherID, ProjectID, RoleType) 
values("Thor", "God of Thunder", 1, 3, "perm2");

insert into Student 
(FirstName, LastName, TeacherID, ProjectID, RoleType) 
values("T'Challa", "T'Challa", 1, 3, "perm2");

insert into Student 
(FirstName, LastName, TeacherID, ProjectID, RoleType) 
values("Janet", "Van Dyne", 1, 3, "perm2");

create table Award(
    AwardID INTEGER,
    StudentID INTEGER,
    apple_type varchar(20),
    ProjectName varChar(30),
    DateAwarded TEXT,

    PRIMARY KEY (AwardID),
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (apple_type) REFERENCES AppleType(apple_type)
);

insert into Award ("AwardID", "StudentID", "apple_type", "ProjectName", "DateAwarded") 
values ('4', '1', 'Rotten', 'Building Phase Project', '2020-01-03 04:02:.22');

insert into Award ("AwardID", "StudentID", "apple_type", "ProjectName", "DateAwarded") 
values ('5', '1', 'Red', 'HoneyPot Project', '2020-01-09 04:02:.22');

insert into Award ("AwardID", "StudentID", "apple_type", "ProjectName", "DateAwarded") 
values ('6', '1', 'Silver', 'Infra Availability Project', '2020-01-06 04:02:.22');

insert into Award ("AwardID", "StudentID", "apple_type", "ProjectName", "DateAwarded") 
values ('7', '1', 'Golden', 'Final Project', '2020-01-20 04:02:.22');

insert into Award ("AwardID", "StudentID", "apple_type", "ProjectName", "DateAwarded") 
values ('8', '1', 'Golden', 'Database Schema Project', '2020-01-30 04:02:.22');

insert into Award ("AwardID", "StudentID", "apple_type", "ProjectName", "DateAwarded") 
values ('9', '1', 'Golden', 'Web App Project', '2020-02-03 04:02:.22');

insert into Award ("AwardID", "StudentID", "apple_type", "ProjectName", "DateAwarded") 
values ('10', '1', 'Golden', 'Python Project', '2020-02-04 10:02:.22');

insert into Award ("AwardID", "StudentID", "apple_type", "ProjectName", "DateAwarded") 
values ('11', '1', 'Golden', 'Flask Project', '2020-02-12 05:12:.22');

insert into Award ("AwardID", "StudentID", "apple_type", "ProjectName", "DateAwarded") 
values ('12', '1', 'Golden', 'Organization Structure Poject', '2020-02-20 09:02:.22');


insert into Award ("AwardID", "StudentID", "apple_type", "ProjectName", "DateAwarded") 
values ('13', '1', 'Golden', 'Initial Planning Project', '2020-02-24 03:02:.22');

insert into Award ("AwardID", "StudentID", "apple_type", "ProjectName", "DateAwarded") 
values ('14', '1', 'Silver', 'Deployment Project', '2020-03-03 07:02:.22');

insert into Award ("AwardID", "StudentID", "apple_type", "ProjectName", "DateAwarded") 
values ('15', '1', 'Silver', 'Security Project', '2020-03-13 10:02:.22');

insert into Award ("AwardID", "StudentID", "apple_type", "ProjectName", "DateAwarded") 
values ('16', '1', 'Silver', 'Application Project', '2020-03-23 3:12:.22');

insert into Award ("AwardID", "StudentID", "apple_type", "ProjectName", "DateAwarded") 
values ('17', '1', 'Silver', 'Pen Testing Proj', '2020-03-28 09:02:.22');

insert into Award ("AwardID", "StudentID", "apple_type", "ProjectName", "DateAwarded") 
values ('18', '1', 'Silver', 'Create Blue Team Project', '2020-04-03 09:32:.22');

insert into Award ("AwardID", "StudentID", "apple_type", "ProjectName", "DateAwarded") 
values ('19', '1', 'Silver', 'Create Red Team Proj', '2020-04-13 03:32:.22');

insert into Award ("AwardID", "StudentID", "apple_type", "ProjectName", "DateAwarded") 
values ('20', '1', 'Red', 'Catch The Hacker Project', '2020-04-23 03:32:.22');

insert into Award ("AwardID", "StudentID", "apple_type", "ProjectName", "DateAwarded") 
values ('21', '1', 'Red', 'Vulnerability Scanner Project', '2020-05-03 03:02:.21');

insert into Award ("AwardID", "StudentID", "apple_type", "ProjectName", "DateAwarded") 
values ('22', '1', 'Red', 'Threat Assesment Project', '2020-05-13 12:12:.21');

insert into Award ("AwardID", "StudentID", "apple_type", "ProjectName", "DateAwarded") 
values ('23', '1', 'Red', 'Install HVAC Project', '2020-05-23 05:42:.21');

insert into Award ("AwardID", "StudentID", "apple_type", "ProjectName", "DateAwarded") 
values ('24', '1', 'Red', 'Team Building Project', '2020-05-30 11:32:.21');

insert into Award ("AwardID", "StudentID", "apple_type", "ProjectName", "DateAwarded") 
values ('25', '1', 'Red', 'Budget Planning Project', '2020-06-03 09:32:.41');

insert into Award ("AwardID", "StudentID", "apple_type", "ProjectName", "DateAwarded") 
values ('26', '1', 'Red', 'Test Deployment Project', '2020-06-13 03:02:.21');

insert into Award ("AwardID", "StudentID", "apple_type", "ProjectName", "DateAwarded") 
values ('27', '1', 'Red', 'Dev Project', '2020-06-23 05:04:.01');

insert into Award ("AwardID", "StudentID", "apple_type", "ProjectName", "DateAwarded") 
values ('28', '1', 'Red', 'Centric Project', '2020-06-30 09:12:.21');

insert into Award ("AwardID", "StudentID", "apple_type", "ProjectName", "DateAwarded") 
values ('2', '2', 'Red', 'ExampleProject', 'YYYY-MM-DD HH:MM:SS.SSS');

insert into Award ("AwardID", "StudentID", "apple_type", "ProjectName", "DateAwarded") 
values ('1', '3', 'Silver', 'ExampleProject', 'YYYY-MM-DD HH:MM:SS.SSS');

insert into Award ("AwardID", "StudentID", "apple_type", "ProjectName", "DateAwarded") 
values ('3', '3', 'Rotten', 'ExampleProject', 'YYYY-MM-DD HH:MM:SS.SSS');



create table Branch(
    BranchID INTEGER,
    StudentID INTEGER,
    ProjectID INTEGER,
    BranchDescription TEXT, 
    Resolved INTEGER,
    Weight INTEGER, 
    
    Primary KEY (BranchID, StudentID, ProjectID),
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (ProjectID) REFERENCES Project(ProjectID)
);

insert into Branch 
(BranchID, StudentID, ProjectID, BranchDescription, Resolved, Weight) 
values(1, 3, 2, "Add colors", 0, 100);

insert into Branch 
(BranchID, StudentID, ProjectID, BranchDescription, Resolved, Weight) 
values(2, 1, 1, "Update ppt", 1, 25);

insert into Branch 
(BranchID, StudentID, ProjectID, BranchDescription, Resolved, Weight) 
values(3, 2, 2, "Change font in document", 1, 25);

insert into Branch 
(BranchID, StudentID, ProjectID, BranchDescription, Resolved, Weight) 
values(3, 3, 2, "Reformat document", 1, 25);

insert into Branch 
(BranchId, StudentID, ProjectID, BranchDescription, Resolved, Weight) 
values (1, 1, 1, "Add pictures", 0, 10);


insert into Branch 
(BranchId, StudentID, ProjectID, BranchDescription, Resolved, Weight) 
values (3, 5, 1, "Change font in document", 0, 5);


insert into Branch 
(BranchID, StudentID, ProjectID, BranchDescription, Resolved, Weight) 
values (2, 5, 1, "Update ppt", 1, 25);

insert into Branch 
(BranchID, StudentID, ProjectID, BranchDescription, Resolved, Weight) 
values (2, 6, 1, "Update ppt", 1, 25);

insert into Branch 
(BranchId, StudentID, ProjectID, BranchDescription, Resolved, Weight) 
values (1, 7, 1, "Add pictures", 0, 10);

insert into Branch 
(BranchId, StudentID, ProjectID, BranchDescription, Resolved, Weight) 
values (1, 11, 3, "Construct clay models", 1, 25);

insert into Branch 
(BranchId, StudentID, ProjectID, BranchDescription, Resolved, Weight) 
values (1, 8, 3, "Construct clay models", 1, 25);

insert into Branch 
(BranchId, StudentID, ProjectID, BranchDescription, Resolved, Weight) 
values (1, 9, 3, "Construct clay models", 1, 25);

insert into Branch 
(BranchId, StudentID, ProjectID, BranchDescription, Resolved, Weight) 
values (2, 8, 3, "Paint models", 0, 10);

insert into Branch 
(BranchId, StudentID, ProjectID, BranchDescription, Resolved, Weight) 
values (3, 10, 3, "Make diorama base", 0, 35);


create table Task(
    TaskID INTEGER,
    BranchID INTEGER,
    StudentID INTEGER, 
    ProjectID INTEGER,
    TaskDescription TEXT,
    Resolved INTEGER,

    PRIMARY KEY (TaskId),
    FOREIGN KEY (BranchID) REFERENCES Branch(BranchID),
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (ProjectID) REFERENCES Project(ProjectID)
);

insert into Task
(BranchID, StudentID, ProjectID, TaskDescription, Resolved)
values(2, 1, 1, "Open power point", 1);

insert into Task
(BranchID, StudentID, ProjectID, TaskDescription, Resolved)
values(3, 2, 2, "Open ms word", 1);

insert into Task
(BranchID, StudentID, ProjectID, TaskDescription, Resolved)
values(3, 3, 2, "Click reformat button", 0);

insert into Task
(BranchID, StudentID, ProjectID, TaskDescription, Resolved)
values(2, 5, 1, "Add picture to powerpoint", 0);

insert into Task
(BranchID, StudentID, ProjectID, TaskDescription, Resolved)
values(2, 6, 1, "Close powerpoint", 0);


insert into Task
(BranchID, StudentID, ProjectID, TaskDescription, Resolved)
values(3, 5, 1, "Choose better font", 0);

insert into Task
(BranchID, StudentID, ProjectID, TaskDescription, Resolved)
values(1, 11, 3, "Purchase clay", 1);

insert into Task
(BranchID, StudentID, ProjectID, TaskDescription, Resolved)
values(1, 11, 3, "Sculpt models", 1);

insert into Task
(BranchID, StudentID, ProjectID, TaskDescription, Resolved)
values(2, 8, 3, "Buy paint", 0);

insert into Task
(BranchID, StudentID, ProjectID, TaskDescription, Resolved)
values(3, 10, 3, "Construct base out of balsa wood", 0);


create table Chat(
    ChatID INTEGER,
    UserName TEXT,
    TaskID INTEGER,
    TimeStamp TEXT,
    MessageString TEXT,

    PRIMARY KEY (ChatID),
    FOREIGN KEY (UserName) REFERENCES UserCredentials(UserName),
    FOREIGN KEY (TaskID) REFERENCES Task(TaskID)
);

insert into Chat
(UserName, TaskID, TimeStamp, MessageString)
values("Wanda Maximoff", 6, "01/19/20 05:34:14 AM", "All done with task number 6! You can format document now. ");

insert into Chat
(UserName, TaskID, TimeStamp, MessageString)
values("Tony Stark", 1, "01/20/20 08:34:29 PM", "Hurry up you bum!");

create table Admin(
    AdminID INTEGER,
    Name varchar(20),
    RoleType varchar(20),

    PRIMARY KEY (AdminID),
    FOREIGN KEY (RoleType) REFERENCES RoleType(permission_level)
);

insert into Admin(Name, RoleType) values("The Watcher", "perm0");

create table UserCredentials(
    UserCredentialsID INTEGER,
    UserID INTEGER,
    UserType varchar(20),
    UserName varchar(20),
    UserPass varchar(20),

    PRIMARY KEY (UserCredentialsID)
);

insert into UserCredentials
(UserID, UserType, UserName, UserPass) 
values(1, "Student", "tom", "1234");

insert into UserCredentials
(UserID, UserType, UserName, UserPass) 
values(1, "Teacher", "BuckyB101", "wwII");

insert into UserCredentials
(UserID, UserType, UserName, UserPass) 
values(7, "Student", "pm", "zoom");

insert into UserCredentials
(UserID, UserType, UserName, UserPass) 
values(11, "Student", "jd", "wasp");

create table Files (
    FileID INTEGER PRIMARY KEY,
    TaskID INTEGER,
    FileName TEXT NOT NULL,
    FileType blob,

    FOREIGN KEY (TaskID) REFERENCES Task(TaskID)
);

create table ProjectGoal(
    GoalID INTEGER,
    ProjectID INTEGER,
    ProjectTargetWeight INTEGER,

    PRIMARY KEY (GoalID),
    FOREIGN KEY (ProjectID) REFERENCES Project(ProjectID)
);

insert into ProjectGoal
(ProjectID, ProjectTargetWeight)
values(3, 70);

insert into ProjectGoal
(ProjectID, ProjectTargetWeight)
values(1, 100);

insert into ProjectGoal
(ProjectID, ProjectTargetWeight)
values(2, 100);



CREATE TRIGGER befor_insert_awards2 BEFORE INSERT ON Award
BEGIN
SELECT CASE 
WHEN ((SELECT StudentID FROM Student WHERE StudentID = NEW.StudentID ) ISNULL) 
THEN RAISE(ABORT, 'This is a User Define Error Message - This ID Does not Exist.') 
END; 
END