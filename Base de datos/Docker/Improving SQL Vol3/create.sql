CREATE TABLE PIECES(
    CODE INTEGER PRIMARY KEY,
    NAME VARCHAR2(50)
);
CREATE TABLE PROVIDERS(
    CODE VARCHAR2(50) PRIMARY KEY,
    NAME VARCHAR2(50)
);
CREATE TABLE PROVIDES (
    PIECE INTEGER,
    PROVIDER VARCHAR2(50),
    PRICE INTEGER,
    CONSTRAINT PIECE_PROVIDER_PK PRIMARY KEY (PIECE, PROVIDER),
    CONSTRAINT PIECE_FK FOREIGN KEY (PIECE) REFERENCES PIECES (CODE),
    CONSTRAINT PROVIDER_FK FOREIGN KEY (PROVIDER) REFERENCES PROVIDERS (CODE)
);