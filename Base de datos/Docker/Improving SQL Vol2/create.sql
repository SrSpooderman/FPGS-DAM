CREATE TABLE DepartametsX(
    Code INTEGER Primary Key,
    Name VARCHAR2(50),
    Budget NUMBER
);
CREATE TABLE EmployeesX(
    SNN INTEGER Primary Key,
    Name VARCHAR2(50),
    LastName VARCHAR2(50),
    Department INTEGER,
    CONSTRAINT DepartmentX_FK FOREIGN KEY (Department) REFERENCES DepartametsX (Code)
);