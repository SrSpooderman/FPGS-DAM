/*Customer*/
/*1*/
SELECT c.CUSTOMER_NAME,c.CUSTOMER_ID,v.VENDOR_NAME
FROM CUSTOMERS c
JOIN VENDORS v where v.CODE = c.VENDOR 
WHERE c.CUSTOMER_TYPE = 'AA';

/*2*/
SELECT C.CUSTOMER_NAME,P.PROVINCE_NAME,V.VENDOR_NAME
FROM CUSTOMERS C
JOIN PROVINCES P ON P.CODE = C.PROVINCE_CODE
JOIN VENDORS V ON C.VENDOR = V.CODE;

/*3*/
CREATE TABLE CATEGORY(
    CAT_PK_CATEGORY NUMBER(2) PRIMARY KEY,
    CAT_BEGINING NUMBER(9),
    CAT_END NUMBER(9)
);
CREATE SEQUENCE CATEGORY_BEGINING_FULL
    START WITH 1
    INCREMENT BY 100000
    MINVALUE 1
    MAXVALUE 1200001
    NOCYCLE;
CREATE SEQUENCE CATEGORY_END_FULL
    START WITH 100000
    INCREMENT BY 100000
    MINVALUE 1
    MAXVALUE 1300000
    NOCYCLE;
CREATE SEQUENCE CATEGORY_PK_FULL
    START WITH 1
    INCREMENT BY 1
    MINVALUE 1
    MAXVALUE 13
    NOCYCLE;
INSERT INTO CATEGORY(CAT_PK_CATEGORY,CAT_BEGINING,CAT_END)
VALUES(CATEGORY_PK_FULL.NEXTVAL,CATEGORY_BEGINING_FULL.NEXTVAL,CATEGORY_END_FULL.NEXTVAL);

SELECT *
FROM CATEGORY;
/*4*/
SELECT C.CUSTOMER_NAME,C.PUCHARSES,CA.CAT_PK_CATEGORY
FROM CUSTOMERS C
JOIN CATEGORY CA ON C.PUCHARSES BETWEEN CA.CAT_BEGINING AND CA.CAT_END
;

/*5*/
SELECT c.*, (c.CAT_BEGINING + c.CAT_END)/2 as average
from CATEGORY c;

/*6*/
SELECT Code,	Name,	Superior_Officer
FROM	Vendor	CONNECT	BY	PRIOR	Code =	Superior_Officer
START	WITH	Code =	'001	';
/**/
SELECT	Code,	Name,	Superior_Officer
FROM	Vendor CONNECT	BY Code =	PRIOR Superior_Officer
START	WITH	Code =	'006	';
/**/

/*7*/