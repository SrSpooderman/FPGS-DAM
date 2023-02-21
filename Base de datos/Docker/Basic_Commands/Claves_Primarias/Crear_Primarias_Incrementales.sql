ALTER TABLE "Tabla" ADD(
    CONSTRAINT "nOMBRE_pk" PRIMARY KEY ("ID dentro de la tabla")
);

CREATE SEQUENCE "NOMBRE_seq" START WITH 1;

CREATE OR REPLACE TRIGGER "NOMBRE_bir"
BEFORE INSERT ON "Tabla"
FOR EACH ROW

BEGIN
    SELECT "Nombre_SEQ".NEXTVAL
    INTO :new."id dentro de la tabla"
    FROM dual;
END;