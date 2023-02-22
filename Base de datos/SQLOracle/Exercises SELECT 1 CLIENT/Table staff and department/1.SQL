CREATE TABLE STAFF(
    Cod_emp INT Primary Key,
    Name_employee VARCHAR2(50) UNIQUE NOT NULL,
    Job VARCHAR2(50) NOT NULL,
    Salary INT NOT NULL,
    Date_Start DATE DEFAULT SYSDATE,
    Cod_dept INT NOT NULL,
    Cod_sup INT DEFAULT 0,
    CONSTRAINT Check_Staff_Job CHECK (Job = 'director' OR Job = 'analyst' OR Job = 'programmer' OR Job = 'project manager'),
    CONSTRAINT Check_Staff_Salary CHECK (Salary BETWEEN 3000 AND 10000),
    CONSTRAINT Dept_FK FOREIGN KEY (Cod_dept) REFERENCES XDEPARMENT (DEPARMENT_CODE),
    CONSTRAINT Sup_FK FOREIGN KEY (Cod_sup) REFERENCES STAFF (Cod_emp)
);