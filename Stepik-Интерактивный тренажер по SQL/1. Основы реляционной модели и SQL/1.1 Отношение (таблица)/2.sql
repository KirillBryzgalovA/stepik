/*
Задание
Занесите новую строку в таблицу book (текстовые значения (тип VARCHAR) заключать либо в двойные, либо в одинарные кавычки):

book_id	title	author	price	amount
INT PRIMARY KEY AUTO_INCREMENT	VARCHAR(50)	VARCHAR(30)	DECIMAL(8,2)	INT
1	Мастер и Маргарита	Булгаков М.А.	670.99	3
*/

INSERT INTO book(title, author, price, amount)
VALUES
  (
    'Мастер и Маргарита',
    'Булгаков М.А.', 670.99,
    3
  );
  SELECT * FROM book;