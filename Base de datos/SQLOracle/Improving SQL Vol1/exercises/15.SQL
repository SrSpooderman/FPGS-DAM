SELECT P.NAME_PRO,P.PRICE
FROM PRODUCTS P
ORDER BY P.PRICE DESC
FETCH NEXT 1 ROWS ONLY;