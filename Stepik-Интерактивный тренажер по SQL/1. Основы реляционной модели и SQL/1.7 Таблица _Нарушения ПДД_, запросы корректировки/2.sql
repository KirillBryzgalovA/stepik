/*
Задание
В таблицу fine первые 5 строк уже занесены. Добавить в таблицу записи с ключевыми значениями 6, 7, 8.

fine_id	name	number_plate	violation	sum_fine	date_violation	date_payment
1	Баранов П.Е.	Р523ВТ	Превышение скорости
(от 40 до 60)	500.00	2020-01-12	2020-01-17
2	Абрамова К.А.	О111АВ	Проезд на
запрещающий сигнал	1000.00	2020-01-14	2020-02-27
3	Яковлев Г.Р.	Т330ТТ	Превышение скорости
(от 20 до 40)	500.00	2020-01-23	2020-02-23
4	Яковлев Г.Р.	М701АА	Превышение скорости
(от 20 до 40)	 	2020-01-12
5	Колесов С.П.	К892АХ	Превышение скорости
(от 20 до 40)	 	2020-02-01
6	Баранов П.Е.	Р523ВТ	Превышение скорости
(от 40 до 60)	 	2020-02-14
7	Абрамова К.А.	О111АВ	Проезд на
запрещающий сигнал	 	2020-02-23
8	Яковлев Г.Р.	Т330ТТ	Проезд на
запрещающий сигнал	 	2020-03-03

Результат
Affected rows: 1

Affected rows: 1

Affected rows: 1

Query result:
+---------------+--------------+----------------------------------+----------+------------------+--------------+
| name          | number_plate | violation                        | sum_fine | date_violation   | date_payment |
+---------------+--------------+----------------------------------+----------+------------------+--------------+
| Баранов П.Е.  | Р523ВТ       | Превышение скорости(от 40 до 60) | 500.00   | 2020-01-12       | 2020-01-17   |
| Абрамова К.А. | О111АВ       | Проезд на запрещающий сигнал     | 1000.00  | 2020-01-14       | 2020-02-27   |
| Яковлев Г.Р.  | Т330ТТ       | Превышение скорости(от 20 до 40) | 500.00   | 2020-01-23       | 2020-02-23   |
| Яковлев Г.Р.  | М701АА       | Превышение скорости(от 20 до 40) | NULL     | 2020-01-12       | NULL         |
| Колесов С.П.  | К892АХ       | Превышение скорости(от 20 до 40) | NULL     | 2020-02-01       | NULL         |
| Баранов П.Е.  | Р523ВТ       | Превышение скорости(от 40 до 60) | NULL     | 2020-02-14       | NULL         |
| Абрамова К.А. | О111АВ       | Проезд на запрещающий сигнал     | NULL     | 2020-02-23       | NULL         |
| Яковлев Г.Р.  | Т330ТТ       | Проезд на запрещающий сигнал     | NULL     | 2020-03-03       | NULL         |
+---------------+--------------+----------------------------------+----------+------------------+--------------+
*/

INSERT INTO fine (fine_id, name, number_plate, violation, sum_fine, date_violation, date_payment)
VALUES(6, "Баранов П.Е.", "Р523ВТ", "Превышение скорости(от 40 до 60)", Null, "2020-02-14", Null);

INSERT INTO fine (fine_id, name, number_plate, violation, sum_fine, date_violation, date_payment)
VALUES(7, "Абрамова К.А.", "О111АВ", "Проезд на запрещающий сигнал", Null, "2020-02-23", Null);

INSERT INTO fine (fine_id, name, number_plate, violation, sum_fine, date_violation, date_payment)
VALUES(8, "Яковлев Г.Р.", "Т330ТТ", "Проезд на запрещающий сигнал", Null, "2020-03-03", Null);