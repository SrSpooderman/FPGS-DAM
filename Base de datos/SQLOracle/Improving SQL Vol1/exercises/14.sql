SELECT M.NAME_MAN
FROM (
    SELECT AVG(P.PRICE) AS AVERAGE_PROD, P.MANUFACTURER AS MANUFACTURES_OBJ
    FROM PRODUCTS P 
    GROUP BY P.MANUFACTURER
)
JOIN MANUFACTURERS M ON MANUFACTURES_OBJ = M.CODE
WHERE AVERAGE_PROD >= 150
;