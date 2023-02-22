CREATE TABLE Customers(
    Customer_ID NUMBER(10) Primary key,
    DNI NUMBER(8),
    Customer_Name VARCHAR2(50),
    Province_code CHAR(2),
    Customer_Type CHAR(2),
    Register_date DATE NOT NULL,
    Vendor NUMBER(3),
    Pucharses INTEGER,
    CONSTRAINT province_FK FOREIGN KEY (Province_code) REFERENCES Provinces (Code)
);
/
CREATE TABLE Purchases(
    Purchase_ID NUMBER(10) Primary key,
    Client NUMBER(10),
    Item NUMBER(10),
    Purchase_Date DATE DEFAULT SYSDATE,
    Amount NUMBER(2),
    CONSTRAINT client_Fk FOREIGN KEY (Client) REFERENCES Customers (Customer_ID),
    CONSTRAINT item_Fk FOREIGN KEY (Item) REFERENCES Items (Code)
);
CREATE TABLE Items(
    Code NUMBER(10) Primary key,
    Description VARCHAR2(60),
    Price NUMBER(3),
    Stock NUMBER(4),
    Origin VARCHAR2(10)
);