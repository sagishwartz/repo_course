--Answer 1
A. RELATIONAL DB build as a structured and orginzed data base. it's build in rows and columns with a unique key identifying each row. 
we can create relations between tables (I hope I understood the question)
B. A collection of database objects. represents the logical configuration of all or part of a relational database

--Answer 2
A+B. SQL  stands for Structured Query Language. SQL is used to communicate with a databas and easy to extract data and to manipulate it (start,stop.update)
C. Used to prevent inserting NULL values into the specified column

--Answer 3
 A. table creation with the name car with 5 columns with the names (each one can contain diff values):
	1. ID - numbers only
	2. Model - Text & Not Null
	3. brand - Text & Not Null & UNIQUE
	4. YEAR - numbers only & Not Null
	5. Price - PK - must contain UNIQUE values, and cannot contain NULL values, at least one should be UNIQUE 
	--- the question here why price was chosen as a UNIQUE and not ID
 B. Add a new row into a table with the name Customer the valuse of 4,'Oren Klein','039865178',05216884651 
	to the column ID,FULLNAME,PHONE_NUMBER,NATIONAL_ID (aligned)
 C. Display rows route and ARRIVAL_TIME from busses table whn value is equal to Egged under company
 D. delete a row in the table products when the values are equal to "sock" and size is larger than 45
 
--Answer 4
A.
	1. table not EXISTS
	2. Table was written differently
B. Value isn't UNIQUE, its exists in different place

--Answer5
A. UPDATE BUSSES SET DESTINATION = 'HOLON' WHERE Comapny = 'Egged';
B. Drop table PRODUCTS;
C. SELECT Color, brand, model FROM Car order by AMOUNT;
D. DELETE FROM BEVERAGES WHERE (SELECT MIN(Vol) AS MaxVoL FROM BEVERAGES);
E. SELECT AIRPLANES.TYPE AS ,AIRPLANE_ID.TYPE  FROM AIRPLANES JOIN FLIGHTS limit 10
f. no idea - to complex for this level and I hopie it will not be in the exam
