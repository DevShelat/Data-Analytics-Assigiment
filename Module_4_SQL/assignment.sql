-- Data Analytics Assignment
-- Module 4: Working with Database using SQL
-- MarketCo Contact Management Database

-- =========================================================
-- QUESTION 1
-- Statement to create the Contact table
-- =========================================================

CREATE TABLE Contact (
    ContactID INT NOT NULL,
    CompanyID INT NULL,
    FirstName VARCHAR(45) NULL,
    LastName VARCHAR(45) NULL,
    Street VARCHAR(45) NULL,
    City VARCHAR(45) NULL,
    State VARCHAR(2) NULL,
    ZIP VARCHAR(10) NULL,
    IsMain BOOLEAN NULL,
    Email VARCHAR(45) NULL,
    Phone VARCHAR(12) NULL,
    PRIMARY KEY (ContactID)
);


-- =========================================================
-- QUESTION 2
-- Statement to create the Employee table
-- =========================================================

CREATE TABLE Employee (
    EmployeeID INT NOT NULL,
    FirstName VARCHAR(45) NULL,
    LastName VARCHAR(45) NULL,
    Salary DECIMAL(10,2) NULL,
    HireDate DATE NULL,
    JobTitle VARCHAR(25) NULL,
    Email VARCHAR(45) NULL,
    Phone VARCHAR(12) NULL,
    PRIMARY KEY (EmployeeID)
);


-- =========================================================
-- QUESTION 3
-- Statement to create the ContactEmployee table
-- ContactDate uses DATE format: YYYY-MM-DD
-- =========================================================

CREATE TABLE ContactEmployee (
    ContactEmployeeID INT NOT NULL,
    ContactID INT NULL,
    EmployeeID INT NULL,
    ContactDate DATE NULL,
    Description VARCHAR(100) NULL,
    PRIMARY KEY (ContactEmployeeID)
);


-- =========================================================
-- QUESTION 4
-- Change Lesley Bland's phone number
-- =========================================================

UPDATE Employee
SET Phone = '215-555-8800'
WHERE FirstName = 'Lesley'
  AND LastName = 'Bland';


-- =========================================================
-- QUESTION 5
-- Change Urban Outfitters, Inc. to Urban Outfitters
-- =========================================================

UPDATE Company
SET CompanyName = 'Urban Outfitters'
WHERE CompanyName = 'Urban Outfitters, Inc.';


-- =========================================================
-- QUESTION 6
-- Remove Dianne Connor's contact event with Jack Lee.
-- This uses the ContactEmployee primary key.
-- The subquery finds the relevant ContactEmployeeID.
-- =========================================================

DELETE FROM ContactEmployee
WHERE ContactEmployeeID = (
    SELECT ContactEmployeeID
    FROM (
        SELECT ce.ContactEmployeeID
        FROM ContactEmployee ce
        JOIN Contact c
          ON ce.ContactID = c.ContactID
        JOIN Employee e
          ON ce.EmployeeID = e.EmployeeID
        WHERE c.FirstName = 'Dianne'
          AND c.LastName = 'Connor'
          AND e.FirstName = 'Jack'
          AND e.LastName = 'Lee'
        LIMIT 1
    ) AS x
);


-- =========================================================
-- QUESTION 7
-- Display the names of employees who have contacted
-- Toll Brothers.
-- Run this in MySQL Workbench and save/copy the actual
-- result shown by your database.
-- =========================================================

SELECT DISTINCT
    e.FirstName,
    e.LastName
FROM Employee e
JOIN ContactEmployee ce
    ON e.EmployeeID = ce.EmployeeID
JOIN Contact c
    ON ce.ContactID = c.ContactID
JOIN Company co
    ON c.CompanyID = co.CompanyID
WHERE co.CompanyName = 'Toll Brothers'
ORDER BY e.LastName, e.FirstName;


-- =========================================================
-- END OF SQL QUESTIONS
-- =========================================================
