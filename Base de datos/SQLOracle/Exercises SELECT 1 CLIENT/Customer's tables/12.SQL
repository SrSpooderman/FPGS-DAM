SELECT C.CUSTOMER_NAME, P.PROVINCE_NAME, TRUNC(C.REGISTER_DATE) - TRUNC(SYSDATE) AS DIAS
FROM CUSTOMERS C
JOIN PROVINCES P ON C.PROVINCE_CODE = P.CODE
ORDER BY DIAS DESC
LIMIT 1;