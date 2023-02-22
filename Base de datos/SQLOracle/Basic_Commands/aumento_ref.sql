CREATE OR REPLACE TRIGGER update_customer_purchases 
AFTER INSERT OR UPDATE ON purchases
FOR EACH ROW 
BEGIN 
    UPDATE Customers 
    SET Pucharses = Pucharses + 1 
    WHERE Customer_ID = :NEW.Client; 
END;