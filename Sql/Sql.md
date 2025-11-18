# 🗄️ SQL

Structured Query Language.

## 🔌 Connect to the Database with MySQL

```bash
  mysql -u <user> -p
```

OR

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
```sql
SELECT * FROM table_name;
SELECT column1, column2 FROM table_name;
SELECT DISTINCT column_name FROM table_name;
SELECT * FROM table_name WHERE column_name = 'value';
SELECT * FROM table_name WHERE column_name LIKE '%pattern%';
SELECT * FROM table_name WHERE column_name IN ('A', 'B', 'C');
SELECT * FROM table_name WHERE column1 = 'A' AND column2 = 'B';
SELECT * FROM table_name ORDER BY column_name DESC;
SELECT * FROM table_name LIMIT 10 OFFSET 20;
SELECT * FROM table_name LIMIT 20, 10;  -- Alternative syntax: LIMIT offset, count
```

### 🧮 Aggregation & Grouping
```sql
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
```sql
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

-- FULL JOIN (not supported in MySQL, use UNION of LEFT and RIGHT)
SELECT * FROM table1
LEFT JOIN table2 ON table1.id = table2.id
UNION
SELECT * FROM table1
RIGHT JOIN table2 ON table1.id = table2.id;
```

### ✍🏼 Insert / Update / Delete / Truncate
```sql
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');
INSERT INTO users VALUES (NULL, 'Bob', 'bob@example.com', NOW());

UPDATE users SET email = 'new@mail.com' WHERE id = 3;

DELETE FROM users WHERE id = 5;
TRUNCATE TABLE users;
```

### 🧱 Table Management (ALTER, CREATE, DROP)
```sql
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
```sql
SHOW DATABASES;                          -- List all databases
USE database_name;                       -- Switch database
SHOW TABLES;                             -- List all tables in the current database
DESCRIBE table_name;                     -- Show table structure
SHOW COLUMNS FROM table_name;            -- Detailed column info
SELECT LAST_INSERT_ID();                 -- Get last auto-increment ID
SHOW GRANTS FOR 'user'@'localhost';      -- Show user privileges
FLUSH PRIVILEGES;                        -- Reload privileges
```

### 🔍 Subqueries
```sql
-- Subquery in WHERE clause
SELECT name, price
FROM products
WHERE price > (SELECT AVG(price) FROM products);

-- Subquery in FROM clause
SELECT category, avg_price
FROM (
  SELECT category, AVG(price) AS avg_price
  FROM products
  GROUP BY category
) AS category_avg
WHERE avg_price > 100;

-- Subquery with IN
SELECT name
FROM users
WHERE id IN (SELECT user_id FROM orders WHERE total > 1000);

-- Subquery with EXISTS
SELECT name
FROM users u
WHERE EXISTS (SELECT 1 FROM orders o WHERE o.user_id = u.id);
```

### 🔐 Constraints & Foreign Keys
```sql
-- Create table with constraints
CREATE TABLE orders (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  total DECIMAL(10, 2) CHECK (total >= 0),
  status ENUM('pending', 'paid', 'cancelled') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Add foreign key to existing table
ALTER TABLE orders
ADD CONSTRAINT fk_user
FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE;

-- Drop foreign key
ALTER TABLE orders DROP FOREIGN KEY fk_user;
```

### 🔢 CASE WHEN (Conditional Logic)
```sql
-- Simple CASE
SELECT name, price,
  CASE
    WHEN price < 10 THEN 'Cheap'
    WHEN price BETWEEN 10 AND 50 THEN 'Moderate'
    ELSE 'Expensive'
  END AS price_category
FROM products;

-- CASE in aggregation
SELECT category,
  SUM(CASE WHEN status = 'active' THEN 1 ELSE 0 END) AS active_count,
  SUM(CASE WHEN status = 'inactive' THEN 1 ELSE 0 END) AS inactive_count
FROM products
GROUP BY category;
```

### 📊 Views
```sql
-- Create view
CREATE VIEW active_users AS
SELECT id, name, email
FROM users
WHERE status = 'active';

-- Use view
SELECT * FROM active_users;

-- Drop view
DROP VIEW active_users;

-- Replace/update view
CREATE OR REPLACE VIEW active_users AS
SELECT id, name, email, created_at
FROM users
WHERE status = 'active';
```

### 🔐 Indexes (Performance Optimization)
```sql
-- Create index
CREATE INDEX idx_email ON users(email);

-- Create unique index
CREATE UNIQUE INDEX idx_username ON users(username);

-- Create composite index
CREATE INDEX idx_name_email ON users(name, email);

-- Show indexes
SHOW INDEX FROM users;

-- Drop index
DROP INDEX idx_email ON users;
```

### 🔄 Transactions
```sql
-- Start transaction
START TRANSACTION;
-- or
BEGIN;

-- Execute queries
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

-- Commit changes
COMMIT;

-- Or rollback if error
ROLLBACK;

-- Example with error handling
START TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
-- If something goes wrong:
ROLLBACK;
-- Otherwise:
COMMIT;
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
| **Aggregate** | `COUNT(*)`, `AVG(price)`, `SUM(amount)`, `MIN(date)`, `MAX(date)`, `GROUP_CONCAT(name SEPARATOR ', ')`            |

---

## 🔒 Security Best Practices

> ⚠️ **Warning**: Always use prepared statements or parameterized queries to prevent SQL injection attacks.

**❌ Vulnerable code (concatenation):**
```python
query = "SELECT * FROM users WHERE email = '" + user_input + "'"  # DANGEROUS!
```

**✅ Secure code (prepared statements):**
```python
# Python with MySQL
cursor.execute("SELECT * FROM users WHERE email = %s", (user_input,))

# PHP with PDO
$stmt = $pdo->prepare("SELECT * FROM users WHERE email = ?");
$stmt->execute([$user_input]);

# Node.js with mysql2
connection.execute("SELECT * FROM users WHERE email = ?", [user_input]);
```

---

## 📥 Import the Database from a .sql file

```bash
# Basic import
mysql -u root -ppassword <database_name> < <file_name.sql>

# Import with verbose output
mysql -u root -ppassword <database_name> < <file_name.sql> -v

# Import from remote server
mysql -h hostname -u root -ppassword <database_name> < <file_name.sql>
```

## 📤 Export the Database to a .sql file

```bash
# Basic export
mysqldump -u root -ppassword <database_name> > <file_name.sql>

# Export with routines (stored procedures & functions)
mysqldump -u root -ppassword --routines <database_name> > <file_name.sql>

# Export structure only (no data)
mysqldump -u root -ppassword --no-data <database_name> > schema.sql

# Export with single transaction (for InnoDB consistency)
mysqldump -u root -ppassword --single-transaction <database_name> > <file_name.sql>

# Export specific table
mysqldump -u root -ppassword <database_name> <table_name> > table_backup.sql

# Export multiple databases
mysqldump -u root -ppassword --databases db1 db2 db3 > multiple_dbs.sql
```

## 🐘 Local MAMP

```bash
  /Applications/MAMP/Library/bin/mysql --host=localhost -uroot -proot
```
