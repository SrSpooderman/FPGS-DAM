CREATE TABLE XDeparment(
    Deparment_Code NUMBER(2) Primary key,
    Deparment_Name CHAR(50) not null,
    City CHAR(50) not null
);
CREATE TABLE XStaff(
    Employee_Code NUMBER(4) Primary key,
    Employee_Name CHAR(50) not null,
    Job CHAR(50) not null,
    Salary NUMBER(5) not null,
    Deparment_Code NUMBER(2),
    Start_Date DATE not null,
    Superior_Officer NUMBER(4),
    CONSTRAINT dept_FK FOREIGN KEY (Deparment_Code) REFERENCES XDeparment (Deparment_Code),
    CONSTRAINT staff_FK FOREIGN KEY (Superior_Officer) REFERENCES XStaff (Employee_Code)
);