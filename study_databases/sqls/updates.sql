--PDATE table_name
--SET column1 = value1, column2 = value2, ...
--WHERE condition;

UPDATE persons
SET lastname = 'Jung', firstname = 'Hans', address = 'seocho', city = 'seoul'
WHERE personid = 2;