SELECT AVG(P.PRICE), m.NAME_MAN
FROM PRODUCTS P
join MANUFACTURERS m on p.MANUFACTURER = m.CODE
GROUP BY m.NAME_MAN, P.NAME_PRO
;