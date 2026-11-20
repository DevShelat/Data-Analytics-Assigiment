# Module 4 – Working with Database using SQL

## Question 1
The `Contact` table stores contact/person information associated with companies.

See `assignment.sql` for the complete `CREATE TABLE Contact` statement.

## Question 2
The `Employee` table stores employee details such as name, phone, email, salary, hire date and job title.

See `assignment.sql` for the complete `CREATE TABLE Employee` statement.

## Question 3
The `ContactEmployee` table connects contacts and employees and stores the contact date and description.

`ContactDate` is defined using the `DATE` data type so dates can be stored in `YYYY-MM-DD` format.

## Question 4
Lesley Bland's phone number is changed to:

`215-555-8800`

## Question 5
The company name:

`Urban Outfitters, Inc.`

is changed to:

`Urban Outfitters`

## Question 6
The contact event between Dianne Connor and Jack Lee is removed from `ContactEmployee`.

The SQL statement uses `ContactEmployeeID`, the primary key of the table, to identify the record to delete.

## Question 7
The SELECT query joins the relevant tables and displays the first and last names of employees who have contacted Toll Brothers.

The actual result should be copied from MySQL Workbench after the query is executed against the assignment database.

## Question 8 – LIKE operators

In a MySQL `LIKE` condition:

- `%` represents zero or more characters.
- `_` represents exactly one character.

Example:

```sql
WHERE LastName LIKE 'Sm%'
```

matches names beginning with `Sm`.

```sql
WHERE LastName LIKE 'Smi_h'
```

matches a five-character pattern where `_` represents one character.

## Question 9 – Normalization

Normalization is the process of organizing database data into related tables to reduce unnecessary duplication and improve data consistency.

It usually involves dividing information into logical tables and connecting those tables using keys.

## Question 10 – Join in MySQL

A join combines rows from two or more tables using a related column, usually a primary key and foreign key relationship.

For example, an employee record can be connected to a contact event through `EmployeeID`.

## Question 11 – DDL, DCL and DML

**DDL – Data Definition Language**

Used to define or change database structures.

Examples:
- `CREATE`
- `ALTER`
- `DROP`

**DML – Data Manipulation Language**

Used to add, modify, delete and retrieve data.

Examples:
- `INSERT`
- `UPDATE`
- `DELETE`
- `SELECT`

**DCL – Data Control Language**

Used to control access and permissions.

Examples:
- `GRANT`
- `REVOKE`

## Question 12 – JOIN clause

The MySQL `JOIN` clause is used to combine related data from different tables based on a matching condition.

Common types include:

1. **INNER JOIN** – returns matching records from both tables.
2. **LEFT JOIN** – returns all records from the left table and matching records from the right table.
3. **RIGHT JOIN** – returns all records from the right table and matching records from the left table.
4. **CROSS JOIN** – returns combinations of rows from both tables.
5. **SELF JOIN** – joins a table to itself.
