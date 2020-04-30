select * from Project where ProjectID = (select ProjectID from Student where StudentID = 3);
