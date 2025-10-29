# 🗄️ SQL

Structured Query Language.

## 🔌 Connect to the Database with MySQL

```bash
  mysql -u <user> -p
```
or
```bash
  mysql -u <user> -p -h <host> -D <database_name> -e "SQL QUERY"
```

Details of the parameters:
> **-u** ⇒ user
>
> **-p** ⇒ password
>
> **-h** ⇒ address of the MySQL server (ex: localhost, 127.0.0.1, or a remote IP)
>
> **-D** ⇒ <database_name> : database name
>
> **-e** ⇒ "DELETE FROM table_name": executes the SQL command directly

## 🧩 Some Core Examples:

### 🔍 SELECT Queries
```bash
  SELECT * FROM table_name;
  SELECT column1, column2 FROM table_name;
  SELECT DISTINCT column_name FROM table_name;
  SELECT * FROM table_name WHERE column_name = 'value';
  SELECT * FROM table_name WHERE column_name LIKE '%pattern%';
  SELECT * FROM table_name WHERE column_name IN ('A', 'B', 'C');
  SELECT * FROM table_name WHERE column1 = 'A' AND column2 = 'B';
  SELECT * FROM table_name ORDER BY column_name DESC;
  SELECT * FROM table_name LIMIT 10 OFFSET 20;
```

### 🧮 Aggregation & Grouping
```bash
  SELECT COUNT(*) FROM table_name;
  SELECT AVG(price) AS avg_price FROM products;
  SELECT SUM(amount) FROM orders WHERE status = 'paid';
  SELECT category, COUNT(*) FROM products GROUP BY category;
  SELECT category, AVG(price)
  FROM products
  GROUP BY category
  HAVING AVG(price) > 100;
```

### 🔗 Joins
```bash
  -- INNER JOIN
  SELECT t1.id, t2.name
  FROM table1 AS t1
  INNER JOIN table2 AS t2 ON t1.id = t2.table1_id;

  -- LEFT JOIN
  SELECT u.id, o.total
  FROM users AS u
  LEFT JOIN orders AS o ON u.id = o.user_id;

  -- RIGHT JOIN
  SELECT o.id, u.name
  FROM orders AS o
  RIGHT JOIN users AS u ON o.user_id = u.id;

  -- FULL JOIN (not supported in MySQL, use UNION)
  SELECT * FROM table1
  LEFT JOIN table2 ON table1.id = table2.id
  UNION
  SELECT * FROM table1
  RIGHT JOIN table2 ON table1.id = table2.id;
```

### ✍🏼 Insert / Update / Delete / Truncate
```bash
  INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');
  INSERT INTO users VALUES (NULL, 'Bob', 'bob@example.com', NOW());

  UPDATE users SET email = 'new@mail.com' WHERE id = 3;

  DELETE FROM users WHERE id = 5;
  TRUNCATE TABLE users;
```

### 🧱 Table Management (ALTER, CREATE, DROP)
```bash
  -- Create / Drop Database
  CREATE DATABASE my_database;
  DROP DATABASE my_database;

  -- Create Table
  CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
  );

  -- Drop Table
  DROP TABLE users;

  -- Alter Table
  ALTER TABLE users ADD age INT;
  ALTER TABLE users MODIFY age SMALLINT;
  ALTER TABLE users CHANGE COLUMN old_name new_name VARCHAR(255);
  ALTER TABLE users DROP COLUMN temp_field;
```

### ⚙️ Database & Table Information
```bash
  SHOW DATABASES;                          -- List all databases
  USE database_name;                       -- Switch database
  SHOW TABLES;                             -- List all tables in the current database
  DESCRIBE table_name;                     -- Show table structure
  SHOW COLUMNS FROM table_name;            -- Detailed column info
  SELECT LAST_INSERT_ID();                 -- Get last auto-increment ID
  SHOW GRANTS FOR 'user'@'localhost';      -- Show user privileges
  FLUSH PRIVILEGES;                        -- Reload privileges
```

---

## 🧱 Data Types Overview
| Category          | Types                                                                |
| ----------------- | -------------------------------------------------------------------- |
| **Numeric**       | `TINYINT`, `SMALLINT`, `INT`, `BIGINT`, `FLOAT`, `DOUBLE`, `DECIMAL` |
| **String / Text** | `CHAR`, `VARCHAR`, `TEXT`, `TINYTEXT`, `LONGTEXT`, `BLOB`            |
| **Date / Time**   | `DATE`, `DATETIME`, `TIMESTAMP`, `TIME`, `YEAR`                      |
| **Special**       | `ENUM`, `SET`                                                        |

## 🧰 Common Built-in Functions
| Type          | Examples                                                                                                          |
| ------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Math**      | `ABS(-5)`, `ROUND(3.1416, 2)`, `CEIL(2.3)`, `FLOOR(2.9)`, `MOD(10, 3)`                                            |
| **String**    | `CONCAT(first_name, ' ', last_name)`, `LENGTH(name)`, `UPPER(name)`, `LOWER(name)`, `REPLACE(text, 'old', 'new')` |
| **Date/Time** | `NOW()`, `CURDATE()`, `DATE_ADD(NOW(), INTERVAL 7 DAY)`, `DATEDIFF(NOW(), created_at)`                            |
| **Aggregate** | `COUNT(*)`, `AVG(price)`, `SUM(amount)`, `MIN(date)`, `MAX(date)`                                                 |

---

## 📥 Import the Database from a .sql file

```bash
  mysql -u root -ppassword <database_name> < <file_name.sql>
```

## 📤 Export the Database to a .sql file

```bash
  mysqldump -u root -ppassword <database_name> > <file_name.sql>
```

## 🐘 Local MAMP

```bash
  /Applications/MAMP/Library/bin/mysql --host=localhost -uroot -proot
```
