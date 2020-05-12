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

insert into Award 
(StudentID, apple_type, DateAwarded, ProjectName) 
values(3, "Silver", "YYYY-MM-DD HH:MM:SS.SSS", "ExampleProject");

insert into Award 
(StudentID, apple_type, DateAwarded, ProjectName) 
values(2, "Red", "YYYY-MM-DD HH:MM:SS.SSS", "ExampleProject");

insert into Award 
(StudentID, apple_type, DateAwarded, ProjectName) 
values(3, "Rotten", "YYYY-MM-DD HH:MM:SS.SSS", "ExampleProject");

insert into Award 
(StudentID, apple_type, DateAwarded, ProjectName) 
values(1, "Rotten", "YYYY-MM-DD HH:MM:SS.SSS", "ExampleProject");

insert into Award 
(StudentID, apple_type, DateAwarded, ProjectName) 
values(1, "Red", "YYYY-MM-DD HH:MM:SS.SSS", "ExampleProject");

insert into Award 
(StudentID, apple_type, DateAwarded, ProjectName) 
values(1, "Silver", "YYYY-MM-DD HH:MM:SS.SSS", "ExampleProject");

insert into Award 
(StudentID, apple_type, DateAwarded, ProjectName) 
values(1, "Golden", "YYYY-MM-DD HH:MM:SS.SSS", "ExampleProject");

insert into Award 
(StudentID, apple_type, DateAwarded, ProjectName) 
values(1, "Golden", "YYYY-MM-DD HH:MM:SS.SSS", "ExampleProject");

insert into Award 
(StudentID, apple_type, DateAwarded, ProjectName) 
values(1, "Golden", "YYYY-MM-DD HH:MM:SS.SSS", "ExampleProject");

insert into Award 
(StudentID, apple_type, DateAwarded, ProjectName) 
values(1, "Golden", "YYYY-MM-DD HH:MM:SS.SSS", "ExampleProject");

insert into Award 
(StudentID, apple_type, DateAwarded, ProjectName) 
values(1, "Golden", "YYYY-MM-DD HH:MM:SS.SSS", "ExampleProject");

insert into Award 
(StudentID, apple_type, DateAwarded, ProjectName) 
values(1, "Golden", "YYYY-MM-DD HH:MM:SS.SSS", "ExampleProject");

insert into Award 
(StudentID, apple_type, DateAwarded, ProjectName) 
values(1, "Golden", "YYYY-MM-DD HH:MM:SS.SSS", "ExampleProject");

insert into Award 
(StudentID, apple_type, DateAwarded, ProjectName) 
values(1, "Silver", "YYYY-MM-DD HH:MM:SS.SSS", "ExampleProject");

insert into Award 
(StudentID, apple_type, DateAwarded, ProjectName) 
values(1, "Silver", "YYYY-MM-DD HH:MM:SS.SSS", "ExampleProject");

insert into Award 
(StudentID, apple_type, DateAwarded, ProjectName) 
values(1, "Silver", "YYYY-MM-DD HH:MM:SS.SSS", "ExampleProject");

insert into Award 
(StudentID, apple_type, DateAwarded, ProjectName) 
values(1, "Silver", "YYYY-MM-DD HH:MM:SS.SSS", "ExampleProject");

insert into Award 
(StudentID, apple_type, DateAwarded, ProjectName) 
values(1, "Silver", "YYYY-MM-DD HH:MM:SS.SSS", "ExampleProject");

insert into Award 
(StudentID, apple_type, DateAwarded, ProjectName) 
values(1, "Silver", "YYYY-MM-DD HH:MM:SS.SSS", "ExampleProject");

insert into Award 
(StudentID, apple_type, DateAwarded, ProjectName) 
values(1, "Red", "YYYY-MM-DD HH:MM:SS.SSS", "ExampleProject");

insert into Award 
(StudentID, apple_type, DateAwarded, ProjectName) 
values(1, "Red", "YYYY-MM-DD HH:MM:SS.SSS", "ExampleProject");

insert into Award 
(StudentID, apple_type, DateAwarded, ProjectName) 
values(1, "Red", "YYYY-MM-DD HH:MM:SS.SSS", "ExampleProject");

insert into Award 
(StudentID, apple_type, DateAwarded, ProjectName) 
values(1, "Red", "YYYY-MM-DD HH:MM:SS.SSS", "ExampleProject");

insert into Award 
(StudentID, apple_type, DateAwarded, ProjectName) 
values(1, "Red", "YYYY-MM-DD HH:MM:SS.SSS", "ExampleProject");

insert into Award 
(StudentID, apple_type, DateAwarded, ProjectName) 
values(1, "Red", "YYYY-MM-DD HH:MM:SS.SSS", "ExampleProject");

insert into Award 
(StudentID, apple_type, DateAwarded, ProjectName) 
values(1, "Red", "YYYY-MM-DD HH:MM:SS.SSS", "ExampleProject");

insert into Award 
(StudentID, apple_type, DateAwarded, ProjectName) 
values(1, "Red", "YYYY-MM-DD HH:MM:SS.SSS", "ExampleProject");

insert into Award 
(StudentID, apple_type, DateAwarded, ProjectName) 
values(1, "Red", "YYYY-MM-DD HH:MM:SS.SSS", "ExampleProject");

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

create table Files (
    FileID INTEGER PRIMARY KEY,
    TaskID INTEGER,
    FileName TEXT NOT NULL,
    FileType blob,

    FOREIGN KEY (TaskID) REFERENCES Task(TaskID)
);
