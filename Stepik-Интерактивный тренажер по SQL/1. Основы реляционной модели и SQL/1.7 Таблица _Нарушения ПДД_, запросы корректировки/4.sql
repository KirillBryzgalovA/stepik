/*
Задание
Вывести фамилию, номер машины и нарушение только для тех водителей, которые на одной машине нарушили одно и то же правило   два и более раз. При этом учитывать все нарушения, независимо от того оплачены они или нет. Информацию отсортировать в алфавитном порядке, сначала по фамилии водителя, потом по номеру машины и, наконец, по нарушению.
Результат
+---------------+--------------+----------------------------------+
| name          | number_plate | violation                        |
+---------------+--------------+----------------------------------+
| Абрамова К.А. | О111АВ       | Проезд на запрещающий сигнал     |
| Баранов П.Е.  | Р523ВТ       | Превышение скорости(от 40 до 60) |
+---------------+--------------+----------------------------------+

Структура и наполнение таблицы fine (без ключевого столбца) перед выполнением этого шага
+---------------+--------+------------------------------+----------+----------------+--------------+
| name          | number | violation                    | sum_fine | date_violation | date_payment |
|               | _plate |                              |          |                |              |
+---------------+--------+------------------------------+----------+----------------+--------------+
| Баранов П.Е.  | Р523ВТ | Превышение скорости(от 40... | 500.00   | 2020-01-12     | 2020-01-17   |
| Абрамова К.А. | О111АВ | Проезд на запрещающий сигнал | 1000.00  | 2020-01-14     | 2020-02-27   |
| Яковлев Г.Р.  | Т330ТТ | Превышение скорости(от 20... | 500.00   | 2020-01-23     | 2020-02-23   |
| Яковлев Г.Р.  | М701АА | Превышение скорости(от 20... | 500.00   | 2020-01-12     | NULL         |
| Колесов С.П.  | К892АХ | Превышение скорости(от 20... | 500.00   | 2020-02-01     | NULL         |
| Баранов П.Е.  | Р523ВТ | Превышение скорости(от 40... | 1000.00  | 2020-02-14     | NULL         |
| Абрамова К.А. | О111АВ | Проезд на запрещающий сигн...| 1000.00  | 2020-02-23     | NULL         |
| Яковлев Г.Р.  | Т330ТТ | Проезд на запрещающий сигн...| 1000.00  | 2020-03-03     | NULL         |
+---------------+--------+------------------------------+----------+----------------+--------------+
*/


SELECT name, number_plate, violation
FROM fine
GROUP BY name, number_plate, violation
HAVING COUNT(*)>=2
ORDER BY name, number_plate, violation
