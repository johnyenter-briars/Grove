-- DDL Code to Grove database

-- --1: Generate Apple Types
-- create table AppleTypes(
--     apple_type varchar(20) PRIMARY KEY
-- );

-- insert into AppleTypes values("Golden");
-- insert into AppleTypes values("Silver");
-- insert into AppleTypes values("Red");
-- insert into AppleTypes values("Rotten");

-- --2: Generate Role Types
-- create table RoleTypes(
--     permission_level varchar(20) PRIMARY KEY
-- );

-- insert into RoleTypes values("perm0");
-- insert into RoleTypes values("perm1");
-- insert into RoleTypes values("perm2");
-- insert into RoleTypes values("perm3");

--3: Generate Teacher table
-- create table Teachers(
--     TeacherID INTEGER,
--     FirstName varchar(20) not null,
--     LastName varchar(20) not null,
--     PermissionLevel varchar(20),
--     PRIMARY key (TeacherID),
--     FOREIGN KEY (PermissionLevel) REFERENCES RoleTypes(permission_level)
-- );

-- insert into Teachers (FirstName, LastName, PermissionLevel) values("Bucky", "Barnes", "perm0");
-- insert into Teachers (FirstName, LastName, PermissionLevel) values("Gamora", "Titan", "perm1");
-- insert into Teachers (FirstName, LastName, PermissionLevel) values("Peter", "Quill", "perm2");
