CREATE OR REPLACE TRIGGER "NOMBRE_bir"
BEFORE INSERT ON "Tabla"
FOR EACH ROW

BEGIN
    SELECT "Nombre_SEQ".NEXTVAL
    INTO :new."id dentro de la tabla"
    FROM dual;
END;