Bir Gharti
Instructor: Zayn Hussain
SQL Practice Assessment
Scenario
You are working for an e-commerce company.
 You have 3 tables:
●	Customers
●	Orders
●	Products
Students need to solve queries using:
●	WHERE
●	JOIN
●	GROUP BY
●	HAVING
●	RANK / DENSE_RANK
1. Create Tables
CREATE TABLE customers (
   customer_id INT,
   customer_name VARCHAR(50),
   city VARCHAR(50)
);

CREATE TABLE products (
   product_id INT,
   product_name VARCHAR(50),
   category VARCHAR(50),
   price DECIMAL(10,2)
);

CREATE TABLE orders (
   order_id INT,
   customer_id INT,
   product_id INT,
   quantity INT,
   order_date DATE
);

2. Insert Sample Data
Customers
INSERT INTO customers VALUES
(1, 'Rahul', 'Mumbai'),
(2, 'Anjali', 'Delhi'),
(3, 'Aman', 'Pune'),
(4, 'Sneha', 'Bangalore'),
(5, 'Karan', 'Mumbai');
Products
INSERT INTO products VALUES
(101, 'Laptop', 'Electronics', 70000),
(102, 'Phone', 'Electronics', 40000),
(103, 'Chair', 'Furniture', 5000),
(104, 'Desk', 'Furniture', 12000),
(105, 'Headphones', 'Electronics', 3000);
Orders
INSERT INTO orders VALUES
(1001, 1, 101, 1, '2026-01-10'),
(1002, 1, 105, 2, '2026-01-11'),
(1003, 2, 102, 1, '2026-01-12'),
(1004, 3, 103, 4, '2026-01-13'),
(1005, 4, 104, 1, '2026-01-14'),
(1006, 5, 101, 1, '2026-01-15'),
(1007, 2, 105, 3, '2026-01-16'),
(1008, 3, 102, 1, '2026-01-17'),
(1009, 1, 103, 2, '2026-01-18'),
(1010, 4, 105, 5, '2026-01-19');

SQL Questions
Beginner Level
Q1.
Show all customers from Mumbai.
Answer: 
SELECT *
FROM customers
WHERE city = 'Mumbai';
Q2.
Show all products with price greater than 10000.
Answer:
SELECT *
FROM products
WHERE price > 1000;
Q3.
Show all Electronics products.
Answer:
SELECT *
FROM products
WHERE category = ‘Electronics’;
Q4.
Show orders placed after 2026-01-14.
Answer:
SELECT *
FROM orders

WHERE order_date > ‘2026-01-14’;


JOIN Questions
Q5.
Answer:
Display customer name and order date for all orders.
SELECT c.customer_name, o.order_date
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id;
Q6.
Show customer name, product name, and quantity ordered.
Answer:
SELECT c.customer_name, p.product_name, o.quantity
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
LEFT JOIN products p ON o.product_id = p.product_id;
Q7.
Display all customers who purchased a Laptop.
Answer:
SELECT distict c.customer_name
FROM customers c
INNER JOIN orders o ON c.customer_id = o.order_id
INNER JOIN products p ON o.product_id = p.product_id
WHERE p.product_name = ‘Laptop’;

Q8.
Show total amount spent for each order.
(Hint: quantity × price)
Answer:
SELECT o.order_id, o.quantity * p.price As total_amount
FROM orders o
INNER JOIN  products p  ON o.product_id = p.product_id;
GROUP BY Questions
Q9.
Find total quantity ordered for each product.
Answer:
SELECT p.product_name, SUM(o.quantity) AS total_quantity
FROM orders o
INNER JOIN products p ON o.product_id = p.product_id
GROUP BY p.product_name;
Q10.
Find total sales amount for each category.
Answer:
SELECT p.category, SUM(o.quantity * p.price) AS total_sales
FROM orders o
INNER JOIN products p ON o.product_id = p.product_id
GROUP BY p.category;
Q11.
Find total number of orders placed by each customer.
Answer:
SELECT c.customer_name, COUNT(o.order_id) AS total_orders
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_name;
Q12.
Show average product price by category.
Answer:
SELECT category, AVG(price) AS average_price
FROM products
GROUP BY category;

HAVING Questions
Q13.
Show categories where total sales amount is greater than 50000.
Answer:
SELECT p.category, SUM(o.quantity * p.price) AS total_sales
FROM orders o
INNER JOIN products p ON o.product_id = p.product_id
GROUP BY p.category
HAVING SUM(o.quantity * p.price) > 50000;
Q14.
Find customers who placed more than 2 orders.
Answer:
SELECT c.customer_name, COUNT(o.order_id) AS total_orders
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_name
HAVING COUNT(o.order_id) > 2;
Q15.
Show products where total quantity sold is greater than 3.
Answer:
SELECT p.product_name, SUM(o.quantity) AS total_quantity
FROM orders o
INNER JOIN products p ON o.product_id = p.product_id
GROUP BY p.product_name
HAVING SUM(o.quantity) > 3;
RANK / DENSE_RANK Questions
Q16.
Rank products based on price (highest first).
Use:
●	RANK()
●	DENSE_RANK()
Answer:
SELECT product_name, price,
       RANK() OVER (ORDER BY price DESC) AS rank_num,
       DENSE_RANK() OVER (ORDER BY price DESC) AS dense_rank_num
FROM products;
Q17.
Find top 2 most expensive products.
Answer:
SELECT product_name, price
FROM products
ORDER BY price DESC
LIMIT 2;
Q18.
Rank customers based on total spending.
Answer:
SELECT c.customer_name,
       SUM(o.quantity * p.price) AS total_spent,
       RANK() OVER (ORDER BY SUM(o.quantity * p.price) DESC) AS spending_rank
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
INNER JOIN products p ON o.product_id = p.product_id
GROUP BY c.customer_name;
-----------------------Thank You--------------------

