/*Archivo para ejecutar codigo*/
CREATE SEQUENCE DATOS_NUM
INCREMENT BY 10
START WITH 1000
MAX VALUE 1050;

INSERT INTO ITEMS
(CODE, DESCRIPTION, PRICE, STOCK, ORIGIN)
VALUES(DATOS_NUM.NEXTVAL);