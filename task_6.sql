-- task_6.sql - Insert multiple customer records
-- Inserting three customers as specified

INSERT INTO customers (
    customer_id, 
    customer_name, 
    email, 
    address
) 
VALUES 
-- Customer 2
(
    2, 
    'Blessing Malik', 
    'bmalik@sandtech.com', 
    '124 Happiness  Ave.'
),
-- Customer 3
(
    3, 
    'Obed Ehoneah', 
    'eobed@sandtech.com', 
    '125 Happiness  Ave.'
),
-- Customer 4
(
    4, 
    'Nehemial Kamolu', 
    'nkamolu@sandtech.com', 
    '126 Happiness  Ave.'
);