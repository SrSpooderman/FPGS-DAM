SELECT P.PROVINCE_NAME, SUM(PUR.PURCHASE_ID)
FROM PROVINCES P
JOIN CUSTOMERS C ON C.PROVINCE_CODE = P.CODE
JOIN PURCHASES PUR ON PUR.CLIENT = C.CUSTOMER_ID
GROUP BY P.PROVINCE_NAME;