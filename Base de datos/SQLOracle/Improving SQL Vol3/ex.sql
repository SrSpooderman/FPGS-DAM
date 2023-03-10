/*1*/
SELECT P.NAME
FROM PIECES P;
/*2*/
SELECT *
FROM PROVIDERS;
/*3*/
SELECT AVG(P.PRICE), P.PIECE
FROM PROVIDES P
GROUP BY P.PIECE;
/*4*/
SELECT PR.NAME
FROM PROVIDERS PR
WHERE PR.CODE IN (SELECT PROVIDER FROM PROVIDES WHERE PIECE = 1);

SELECT PR.NAME
FROM PROVIDES P
JOIN PROVIDERS PR ON PR.CODE = P.PROVIDER
WHERE P.PIECE = 1;
/*5*/
SELECT PI.NAME
FROM PROVIDES PR
JOIN PIECES PI ON PI.CODE = PR.PIECE
WHERE PR.PROVIDER = 'HAL';

SELECT PI.NAME
FROM PIECES PI
WHERE PI.CODE IN (SELECT PIECE FROM PROVIDES WHERE PROVIDER = 'HAL');

SELECT PI.NAME
FROM PIECES PI
WHERE EXISTS (SELECT PROVIDER FROM PROVIDES WHERE PROVIDES.PIECE = PI.CODE AND PROVIDER = 'HAL');
/*6*/
SELECT PI.NAME, P.NAME, PR.PRICE
FROM PROVIDES PR
JOIN PIECES PI ON PI.CODE = PR.PIECE
JOIN PROVIDERS P ON P.CODE = PR.PROVIDER
WHERE PR.PRICE = (
    SELECT MAX(PR2.PRICE)
    FROM PROVIDES PR2
    WHERE PR.PIECE = PR2.PIECE
);
/*7*/
INSERT INTO Provides(Piece, Provider, Price) VALUES(1,'TNBC',7);
/*8*/
UPDATE PROVIDES
SET PRICE = PRICE+1;
/*9*/
DELETE FROM PROVIDES
WHERE PROVIDER = 'RBT' AND PIECE = 4;
/*10*/
DELETE PROVIDES
WHERE PROVIDER = 'RBT';